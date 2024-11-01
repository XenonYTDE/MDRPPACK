# I wrote this drunk on a friday afternoon. What the fuck do you expect from a degen
# I dont fucking care about edge cases and you can go fuck yourself
# Files were edited to remove `equipment_modules = {}` block identifier because fuck i'm too lazy to work anymore on this stupid ass shit

import re

properties = [
    "abbreviation",
    "category",
    "sfx",
    "xp_cost",
    "manpower",
    "dismantle_cost_ic",
]
nested_properties = [
    "can_convert_from",
    "build_cost_resources",
    "add_stats",
    "multiply_stats",
    "add_average_stats",
    "allow_mission_type",
    "critical_parts",
    "allowed_module_categories",
    "mission_type_stats",
    "add_equipment_type",
    "forbid_equipment_type_exact_match_for_category"
]


def parse_modules(file):
    result = []
    lines = file.readlines()
    current = None
    current_section = None
    current_mission_type_stats_setting_type = None
    for line_idx, line in enumerate(lines):
        # remove whitespaces, tabs and newlines and other bullshit, and stupid ass fucking comments
        line = re.sub(r'\s*#.*', '', ''.join(line.strip().split()))
        if not line or line.startswith("#"):
            continue
        if line.startswith("}"):
            # thank god for the fucking formatter. all new modules have a \n before them
            prev_line = lines[line_idx - 1].strip() if line_idx > 0 else None
            next_line = lines[line_idx + 1].strip() if line_idx + \
                1 < len(lines) else None
            if line_idx == len(lines) - 1 or not next_line:
                result.append(current)
                current = None
                current_section = None
                current_mission_type_stats_setting_type = None
                continue
            elif prev_line is not None and prev_line.startswith("}"):
                current_section = None
                current_mission_type_stats_setting_type = None
        match = re.match(r'(\w+)\s*=\s*{', line)
        if match and current is None:
            current = {"token": match.group(1)}
            continue
        key_val_match = re.match(r'\s*(\w+)\s*=\s*(.*)', line)
        if key_val_match:
            key, value = key_val_match.groups()
            if key in properties:
                current[key] = value if (key is not None and value is not None) else None
                current_section = None
                current_mission_type_stats_setting_type = None
            elif key in nested_properties and current_section != "mission_type_stats":
                current_section = key
                current_mission_type_stats_setting_type = None
                if key == "can_convert_from" or key == "allow_mission_type" or key == "critical_parts" or key == "allowed_module_categories" or key == "mission_type_stats" or key == "forbid_equipment_type_exact_match_for_category":
                    if key not in current:
                        current[key] = []
                elif key == "add_equipment_type":
                    if value == "{":
                        current[key] = []
                    else:
                        current[key] = [value]
                        current_section = None
                else:
                    current[key] = {}
            elif current_section == "can_convert_from":
                if key == "convert_cost_ic":
                    current[current_section][len(
                        current[current_section]) - 1][key] = value
                else:
                    current[current_section].append({key: value})
            elif current_section == "allowed_module_categories":
                current[current_section].append(
                    {"name": key, "allowed": []})
            elif current_section == "mission_type_stats":
                if current_mission_type_stats_setting_type is None or key == "mission_type_stats":
                    current[current_section].append(
                        {"limit": [], "add_stats": {}, "multiply_stats": {}, "add_average_stats": {}})
                if key == "limit" or key == "add_stats" or key == "multiply_stats" or key == "add_average_stats":
                    current_mission_type_stats_setting_type = key
                if current_mission_type_stats_setting_type is not None and "{" not in line:
                    current[current_section][len(
                        current[current_section])-1][current_mission_type_stats_setting_type][key] = value
            elif current_section == "forbid_equipment_type_exact_match_for_category":
                current[current_section].append([key, value])
            elif current_section is not None:
                current[current_section][key] = value
                current_mission_type_stats_setting_type = None
        elif not line.startswith("}"):
            if current_section == "allow_mission_type":
                current["allow_mission_type"].append(line)
            elif current_section == "critical_parts":
                current["critical_parts"].append(line)
            elif current_section == "add_equipment_type":
                current["add_equipment_type"].append(line)
            elif current_section == "allowed_module_categories":
                current[current_section][len(
                    current[current_section])-1]["allowed"].append(line)
            elif current_section == "mission_type_stats":
                # should only add those in `limit` section. others should be matched by regex in above block
                current[current_section][len(
                    current[current_section])-1]["limit"].append(line)
    return result


def get_token(token):
    if not token:
        return None
    return re.sub(r'(_gen\d*|_\d*)$', "", token)


def get_abbreviation(abbreviation):
    if not abbreviation:
        return None
    return re.sub(r'(\d)(?=\D*$)', "", abbreviation)


# Like I said, I don't care about edge cases. Fuck you if your module is called blended_wing. Fuck you.
def get_parent(token):
    if not token or token[-1] == "1":
        return None
    match = re.search(r'\d+$', token)
    if match:
        number = int(match.group()) + 1
        return token[:match.start()] + str(number)
    else:
        return token


def get_generation(token):
    generation = token[-1]
    if generation.isdigit():
        return int(generation)
    else:
        return 0


def analyze_modules(modules):
    result = []
    current_token = get_token(modules[0]["token"])
    abbreviation = get_abbreviation(
        modules[0]["abbreviation"]) if "abbreviation" in modules[0] else None
    sfx = modules[0]["sfx"] if "sfx" in modules[0] else None
    category = modules[0]["category"] if "category" in modules[0] else None
    current_module = {
        "token": current_token,
        "abbreviation": abbreviation,
        "sfx": sfx,
        "category": category,
        "instances": []
    }
    for idx, module in enumerate(modules):
        if not current_token in module["token"]:
            result.append(current_module)
            current_token = get_token(module["token"])
            abbreviation = get_abbreviation(
                module["abbreviation"]) if "abbreviation" in module else None
            sfx = module["sfx"] if "sfx" in module else None
            category = module["category"] if "category" in module else None
            current_module = {
                "token": current_token,
                "abbreviation": abbreviation,
                "sfx": sfx,
                "category": category,
                "instances": []
            }
        current_module["instances"].append({
            "name": module["token"],
            "generation": get_generation(module["token"]),
            "parent": get_parent(module["token"]),
            "xp_cost": module["xp_cost"] if "xp_cost" in module else None,
            "manpower": module["manpower"] if "manpower" in module else None,
            "add_equipment_type": module["add_equipment_type"] if "add_equipment_type" in module else None,
            "dismantle_cost_ic": module["dismantle_cost_ic"] if "dismantle_cost_ic" in module else None,
            "can_convert_from": module["can_convert_from"] if "can_convert_from" in module else None,
            "build_cost_resources": module["build_cost_resources"] if "build_cost_resources" in module else None,
            "add_stats": module["add_stats"] if "add_stats" in module else None,
            "multiply_stats": module["multiply_stats"] if "multiply_stats" in module else None,
            "add_average_stats": module["add_average_stats"] if "add_average_stats" in module else None,
            "allow_mission_type": module["allow_mission_type"] if "allow_mission_type" in module else None,
            "allowed_module_categories": module["allowed_module_categories"] if "allowed_module_categories" in module else None,
            "mission_type_stats": module["mission_type_stats"] if "mission_type_stats" in module else None,
            "forbid_equipment_type_exact_match_for_category": module["forbid_equipment_type_exact_match_for_category"] if "forbid_equipment_type_exact_match_for_category" in module else None,
            "critical_parts": module["critical_parts"] if "critical_parts" in module else None
        })
    result.append(current_module)
    return result


def calculate_stat_differences(modules):
    result = []
    for module in modules.copy():
        current = {
            "token": module["token"],
            "stat_differences": {
                "add_stats": {},
                "multiply_stats": {},
                "add_average_stats": {},
                "mission_type_stats": [],
                "build_cost_resources": {}
            }
        }
        for instance in module["instances"]:
            for stat_modifier_type in ["add_stats", "multiply_stats", "add_average_stats"]:
                if stat_modifier_type in instance and instance[stat_modifier_type] is not None:
                    for stat, value in instance[stat_modifier_type].items():
                        if stat in current["stat_differences"][stat_modifier_type]:
                            current["stat_differences"][stat_modifier_type][stat]["values"].append(
                                float(value))
                        else:
                            current["stat_differences"][stat_modifier_type][stat] = {
                                "value": 0,
                                "values": [float(value)]
                            }
            if "mission_type_stats" in instance and instance["mission_type_stats"] is not None:
                for mission_type in instance["mission_type_stats"]:
                    # current["stat_differences"]["mission_type_stats"].append(
                    #     {"limit": mission_type["limit"], "add_stats": {}, "multiply_stats": {}, "add_average_stats": {}})
                    idx = None
                    for _i, _c_mission_type in enumerate(current["stat_differences"]["mission_type_stats"]):
                        if _c_mission_type["limit"] == mission_type["limit"]:
                            idx = _i
                    if idx is None:
                        current["stat_differences"]["mission_type_stats"].append(
                            {"limit": mission_type["limit"], "add_stats": {}, "multiply_stats": {}, "add_average_stats": {}})
                    for stat_type in ["add_stats", "multiply_stats", "add_average_stats"]:
                        if stat_type in mission_type and len(mission_type[stat_type].keys()) > 0:
                            for stat, value in mission_type[stat_type].items():
                                # find the right mission limit list should be the same
                                if stat in current["stat_differences"]["mission_type_stats"][-1][stat_type]:
                                    current["stat_differences"]["mission_type_stats"][-1][stat_type][stat]["values"].append(
                                        float(value))
                                else:
                                    current["stat_differences"]["mission_type_stats"][-1][stat_type][stat] = {
                                        "value": 0,
                                        "values": [float(value)]
                                    }

            if "build_cost_resources" in instance and instance["build_cost_resources"] is not None:
                for resource, value in instance["build_cost_resources"].items():
                    if resource in current["stat_differences"]["build_cost_resources"]:
                        current["stat_differences"]["build_cost_resources"][resource]["values"].append(
                            float(value))
                    else:
                        current["stat_differences"]["build_cost_resources"][resource] = {
                            "value": 0,
                            "values": [float(value)]
                        }
        for stat_modifier_type in ["add_stats", "multiply_stats", "add_average_stats"]:
            for stat, value in current["stat_differences"][stat_modifier_type].items():
                _item = current["stat_differences"][stat_modifier_type][stat]
                diff = (max(_item["values"]) - min(_item["values"]))/(len(_item["values"]) - 1) if len(
                    _item["values"]) > 1 else 0
                _item["value"] = round(diff, 4)
        if len(current["stat_differences"]["mission_type_stats"]) > 0:
            for mission_type_stat in current["stat_differences"]["mission_type_stats"]:
                for stat_type in ["add_stats", "multiply_stats", "add_average_stats"]:
                    if stat_type in mission_type_stat:
                        for stat, value in mission_type_stat[stat_type].items():
                            _item = mission_type_stat[stat_type][stat]
                            diff = (max(_item["values"]) - min(_item["values"]))/(
                                len(_item["values"]) - 1) if len(_item["values"]) > 1 else 0
                            _item["value"] = round(diff, 4)
        for resource, value in current["stat_differences"]["build_cost_resources"].items():
            _item = current["stat_differences"]["build_cost_resources"][resource]
            diff = (max(_item["values"]) - min(_item["values"]))/(len(
                _item["values"]) - 1) if len(_item["values"]) > 1 else 0
            # _item["value"] = round(diff, 6)
            _item["value"] = diff
        result.append(current)
    return result


nested_properties1 = [
    "build_cost_resources",
    "add_stats",
    "multiply_stats",
    "add_average_stats",
    "mission_type_stats",
]


def get_can_convert_from_str(can_convert_from):
    result = ""
    prefix = "\tcan_convert_from = { "
    for item in can_convert_from:
        result += prefix
        for key, value in item.items():
            result += f"{key} = {value} "
        result += "}\n"
    return result


def get_list_type_generated_str(list, generate_type, use_tab=True, use_newline=True):
    result = f"\t{generate_type} = " + \
        "{ " if use_tab else f"{generate_type} = " + "{ "
    for item in list:
        result += f"{item} "
    if not use_newline:
        return result + "}"
    return result + "}\n"


def get_allowed_module_categories_str(allowed_module_categories):
    result = "\tallowed_module_categories = {"
    for item in allowed_module_categories:
        result += f" {get_list_type_generated_str(item['allowed'], item['name'], False, False)}"
    return result + " }\n"


def get_forbid_equipment_type_exact_match_for_category_str(forbid_equipment_type_exact_match_for_category):
    result = "\tforbid_equipment_type_exact_match_for_category = {"
    for item in forbid_equipment_type_exact_match_for_category:
        result += f" {item[0]} = {item[1]}"
    return result + " }\n"


def get_stats_str(stats, stats_difference, generation, stats_type, add_tab=False, resource_cost_advance_generations=None):
    result = "\t\t" if add_tab else "\t"
    result += f"{stats_type} = " + "{\n"
    for key, value in stats.items():
        stat = ""
        if resource_cost_advance_generations is not None:
            advance = 0
            for i in resource_cost_advance_generations:
                if generation >= i:
                    advance += 1
            stat = f"{key} = {round(float(value) + stats_difference[key]['value'] * advance, 3)}"
        else:
            stat = f"{key} = {round(float(value) + stats_difference[key]['value'] * generation, 3)}"
        if (add_tab):
            result += f"\t\t\t{stat}\n"
        else:
            result += f"\t\t{stat}\n"
    if (add_tab):
        return result + "\t\t}\n"
    return result + "\t}\n"


def get_mission_type_stats_str(mission_type_stats, stats_difference, generation):
    result = ""
    for mission_idx, mission_type in enumerate(mission_type_stats):
        result += "\tmission_type_stats = {\n"
        result += f"\t\t{get_list_type_generated_str(mission_type['limit'], 'limit', False, True)}"
        for stat_type in ["add_stats", "multiply_stats", "add_average_stats"]:
            if stat_type in mission_type and len(mission_type[stat_type].keys()) > 0:
                result += f"{get_stats_str(mission_type[stat_type], stats_difference[mission_idx][stat_type], generation, stat_type, True)}"
        result += "\t}\n"
    return result


def generate_your_mom(modules, stat_differences, generation_options):
    # if the file isn't organized correctly it ain't going to fucking work bitch
    contents = []
    items_to_generate = generation_options["items_to_generate"]
    num_to_advance = generation_options["num_to_advance"] if (
        "num_to_advance" in generation_options and generation_options["num_to_advance"] is not None) else 0
    interval = items_to_generate / (num_to_advance + 1)
    start = 0  # range start
    generations_to_advance = [int(start + (i + 1) * interval)
                              for i in range(num_to_advance)]
    for module_idx, module in enumerate(modules):
        instance = module["instances"][-1]
        print(instance["name"])
        prefix = re.sub(r'\d$', "", instance["name"])
        category = f"\tcategory = {module['category']}\n" if module["category"] is not None else ""
        sfx = f"\tsfx = {module['sfx']}\n" if module["sfx"] is not None else ""
        xp_cost = f"\txp_cost = {instance['xp_cost']}\n" if instance["xp_cost"] is not None else ""
        dismantle_cost_ic = f"\tdismantle_cost_ic = {instance['dismantle_cost_ic']}\n" if instance[
            "dismantle_cost_ic"] is not None else ""
        manpower = f"\tmanpower = {instance['manpower']}\n" if instance["manpower"] is not None else ""
        can_convert_from = get_can_convert_from_str(
            instance["can_convert_from"]) if instance["can_convert_from"] is not None else ""
        add_equipment_type = get_list_type_generated_str(
            instance["add_equipment_type"], "add_equipment_type") if instance["add_equipment_type"] is not None else ""
        allow_mission_type = get_list_type_generated_str(
            instance["allow_mission_type"], "allow_mission_type") if instance["allow_mission_type"] is not None else ""
        critical_parts = get_list_type_generated_str(
            instance["critical_parts"], "critical_parts") if instance["critical_parts"] is not None else ""
        allowed_module_categories = get_allowed_module_categories_str(
            instance["allowed_module_categories"]) if instance["allowed_module_categories"] is not None else ""
        forbid_equipment_type_exact_match_for_category = get_forbid_equipment_type_exact_match_for_category_str(
            instance["forbid_equipment_type_exact_match_for_category"]) if instance["forbid_equipment_type_exact_match_for_category"] is not None else ""
        for i in range(items_to_generate):
            current = f"{prefix}{instance['generation'] + i + 1}" + " = {\n"
            abbreviation = re.sub(r'"', "", module['abbreviation']) + str(
                instance['generation'] + i + 1) if module["abbreviation"] is not None else None
            abbreviation_str = f"\tabbreviation = \"{abbreviation}\"\n" if abbreviation is not None else ""
            parent = f"\tparent = {prefix}{instance['generation'] + i}\n"
            current += abbreviation_str + category + sfx + parent + manpower + add_equipment_type + \
                allow_mission_type + allowed_module_categories + \
                forbid_equipment_type_exact_match_for_category + can_convert_from
            add_stats = get_stats_str(
                instance["add_stats"], stat_differences[module_idx]["stat_differences"]["add_stats"], i + 1, "add_stats") if ("add_stats" in instance and instance["add_stats"] is not None) else ""
            multiply_stats = get_stats_str(
                instance["multiply_stats"], stat_differences[module_idx]["stat_differences"]["multiply_stats"], i + 1, "multiply_stats") if ("multiply_stats" in instance and instance["multiply_stats"] is not None) else ""
            add_average_stats = get_stats_str(
                instance["add_average_stats"], stat_differences[module_idx]["stat_differences"]["add_average_stats"], i + 1, "add_average_stats") if ("add_average_stats" and instance["add_average_stats"] is not None) in instance else ""
            mission_type_stats = get_mission_type_stats_str(instance["mission_type_stats"], stat_differences[module_idx]["stat_differences"]["mission_type_stats"], i + 1) if (
                "mission_type_stats" in instance and instance["mission_type_stats"] is not None) else ""
            current += add_stats + multiply_stats + \
                add_average_stats + mission_type_stats + \
                xp_cost + dismantle_cost_ic + critical_parts
            if len(generations_to_advance) > 0:
                build_cost_resources = get_stats_str(
                    instance["build_cost_resources"], stat_differences[module_idx]["stat_differences"]["build_cost_resources"], i + 1, "build_cost_resources", resource_cost_advance_generations=generations_to_advance) if ("build_cost_resources" in instance and instance["build_cost_resources"] is not None) else ""
                current += build_cost_resources
            else:
                build_cost_resources = get_stats_str(
                    instance["build_cost_resources"], stat_differences[module_idx]["stat_differences"]["build_cost_resources"], i + 1, "build_cost_resources") if ("build_cost_resources" in instance and instance["build_cost_resources"] is not None) else ""
                current += build_cost_resources
            current += "}\n"
            contents.append(current)
    return contents


file_names = [
    "MD_arty_modules",
    "MD_helicopter_modules",
    "MD_plane_modules",
    "MD_ship_modules",
    "MD_tank_modules",
    "titan_mods"
]

for file_name in file_names:
    with open(f"{file_name}.txt", 'r') as file:
        result = parse_modules(file)
        modules = analyze_modules(result)
        stat_differences = calculate_stat_differences(modules)
        contents = generate_your_mom(modules, stat_differences, {
            "items_to_generate": 4, "num_to_advance": 1})
        with open(f"generated/generated_{file_name}.txt", 'w') as f:
            for content in contents:
                f.write(content)

# with open('test.txt', 'r') as file:
#     result = parse_modules(file)
#     # print(result)
#     modules = analyze_modules(result)
#     stat_differences = calculate_stat_differences(modules)
#     # print(modules)
#     # print(stat_differences)
#     contents = generate_your_mom(modules, stat_differences, {
#         "items_to_generate": 30, "num_to_advance": 3})
#     with open('modules_generated.txt', 'w') as f:
#         for content in contents:
#             f.write(content)
