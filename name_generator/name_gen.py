import random

name_list = [
    "Nakorn",
    "Phra",
    "Suvarnabhumi",
    "Ayutthaya",
    "Ratchaburi",
    "Bangkok",
    "Chiangmai",
    "Nakhonratchasima",
    "Songkhla",
    "Udonthani",
    "Phuket",
    "Kanchanaburi",
    "Krabi",
    "Rayong",
    "Chanthaburi",
    "Sukhothai",
    "Nakhonsithammarat",
    "Roi-Et",
    "Phitsanulok",
    "Chonburi",
    "Lampang",
    "Nonthaburi",
    "Narathiwat",
    "Ranong",
    "Ubonratchathani",
    "Phangnga",
    "Suratthani",
    "Trang",
    "Samutprakan",
    "Chumphon",
    "Loei",
    "Mae",
    "Nakhonpathom",
    "Prachuapkhiri",
    "Nakhonphanom",
    "Pattani",
    "Yala",
    "Kalasin",
    "Uthai",
    "Chiangrai",
    "Nakhonsawan",
    "Phrae",
    "Satun",
    "Suphanburi",
    "Sisaket",
    "Mukdahan",
    "Trat",
    "Nakhon",
    "Chachoengsao",
    "Chaiyaphum",
    "Chiang",
    "Lamphun",
    "Phayao",
    "Nongbualamphu",
    "Udon",
    "Yasothon",
    "Nongkhai",
    "Amnat",
]

# inclusive
output_range = [4, 8]

air_name_guide = {
    "country": "SIA",
    "carrier_designation": "C", #secondary
    "fighter": "RTA",
    "mr": "RTA",
    "carrier_naval_strike": "RTN",
    "naval_bomber": "NB", #secondary
    "cas": "RTG",
    "transport": "RTT",
    "awacs": "RTA",
    "awacs_secondary": "RTE", #secondary
    "strat_bomber": "RTB",
    "gunship": "G", #secondary
    "naval_patrol": "RTP",
    "unmanned": "THUNDERBIRD ",
    "use_dash": True
}

air_types = {
    "light_as": {
        # name, prefix, [min range, max range], use_name?, use_dash?
        "base": ["small_plane_airframe", air_name_guide["fighter"], [251, 350], True],
        # name, tertiary designation
        "variants": [
            ["cv_small_plane_airframe", None]
        ]
    },
    "light_mr": {
        "base": ["small_plane_strike_airframe", air_name_guide["mr"], [351, 450], True],
        "variants": [
            ["small_plane_naval_bomber_airframe", air_name_guide["naval_bomber"]],
            ["cv_small_plane_strike_airframe", None],
            ["cv_small_plane_naval_bomber_airframe", air_name_guide["naval_bomber"]],
        ]
    },
    "light_cas": {
        "base": ["small_plane_cas_airframe", air_name_guide["cas"], [451, 550], True],
        "variants": [
            ["cv_small_plane_cas_airframe", None]
        ]
    },
    "medium_as": {
        "base": ["medium_plane_fighter_airframe", air_name_guide["fighter"], [151, 250], True],
        "variants": [
            ["cv_medium_plane_fighter_airframe", None]
        ]
    },
    "medium_mr": {
        "base": ["medium_plane_airframe", air_name_guide["mr"], [51, 150], True],
        "variants": [
            ["medium_plane_maritime_patrol_airframe", air_name_guide["naval_bomber"]],
            ["cv_medium_plane_airframe", None],
        ]
    },
    "medium_carrier_naval_strike": {
        "base": ["cv_medium_plane_maritime_patrol_airframe", air_name_guide["carrier_naval_strike"], [51, 150], True],
        "variants": []
    },
    "medium_cas": {
        "base": ["medium_plane_cas_airframe", air_name_guide["cas"], [551, 650], True],
        "variants": [
            ["cv_medium_plane_cas_airframe", None]
        ]
    },
    "medium_lift": {
        "base": ["medium_plane_air_transport_airframe", air_name_guide["transport"], [51, 150], True],
        "variants": [
            ["cv_medium_plane_air_transport_airframe", None],
            ["cv_medium_plane_scout_airframe", air_name_guide["awacs_secondary"]]
        ]
    },
    "large_plane_1": {
        "base": ["large_plane_airframe", air_name_guide["strat_bomber"], [51, 150], True],
        "variants": [
            ["large_plane_cas_airframe", air_name_guide["gunship"]]
        ]
    },
    "large_plane_2": {
        "base": ["large_plane_awacs_airframe", air_name_guide["awacs"], [51, 150], True],
        "variants": []
    },
    "large_plane_3": {
        "base": ["large_plane_maritime_patrol_airframe", air_name_guide["naval_patrol"], [51, 150], True],
        "variants": []
    },
    "large_plane_4": {
        "base": ["large_plane_air_transport_airframe", air_name_guide["transport"], [51, 150], True],
        "variants": []
    },
    "unmanned_drone": {
        "base": ["small_plane_suicide_airframe", air_name_guide["unmanned"], [51, 150], False, False],
        "variants": [
            ["cv_small_plane_suicide_airframe", None]
        ]
    }
}

def generate_air():
    output = []
    prev_model_nums = []
    for key, val in air_types.items():
        prev_model_nums.append(val["base"][2][0])
    for i in range(output_range[0], output_range[1] + 1):
        for _idx, [type_key, type_items] in enumerate(air_types.items()):
            base = type_items["base"]
            model_num = min(prev_model_nums[_idx] + random.randint(1, 12), base[2][1])
            prev_model_nums[_idx] = model_num
            name = "" if not base[3] else " " + name_list.pop(random.randint(0, len(name_list) - 1)) if len(name_list) > 0 else ""
            base_result = base[0] + "_" + str(i) + f": \"{base[1]}{'-' if air_name_guide['use_dash'] and ((len(base) > 4 and base[4] == True) or len(base) < 5) else ''}{model_num}" + name + "\""
            output.append(base_result)
            for variant in type_items["variants"]:
                is_cv = variant[0].startswith('cv')
                result = variant[0] + "_" + str(i) + f": \"{base[1]}{'-' if air_name_guide['use_dash'] and ((len(base) > 4 and base[4] == True) or len(base) < 5) else ''}{model_num}{air_name_guide['carrier_designation'] if is_cv else ''}{variant[1] if variant[1] is not None else ''}" + name + "\""
                output.append(result)
        # print(output)
    output.sort(key=sort_air)
    with open(f"output.txt", 'w') as f:
        for _i, line in enumerate(output):
            out = f"{air_name_guide['country']}_"+line
            out += "\n" if _i != len(output)-1 else ""
            f.write(out)

def sort_air(item):
    val = 0
    factor = output_range[1]
    line_types = [
        "small_plane_airframe",
        "small_plane_strike_airframe",
        "small_plane_cas_airframe",
        "small_plane_naval_bomber_airframe",
        "small_plane_suicide_airframe",
        "cv_small_plane_airframe",
        "cv_small_plane_strike_airframe",
        "cv_small_plane_cas_airframe",
        "cv_small_plane_naval_bomber_airframe",
        "cv_small_plane_suicide_airframe",
        "medium_plane_airframe",
        "medium_plane_fighter_airframe",
        "medium_plane_cas_airframe",
        "medium_plane_maritime_patrol_airframe",
        "medium_plane_air_transport_airframe",
        "medium_plane_suicide_airframe",
        "cv_medium_plane_airframe",
        "cv_medium_plane_fighter_airframe",
        "cv_medium_plane_cas_airframe",
        "cv_medium_plane_maritime_patrol_airframe",
        "cv_medium_plane_air_transport_airframe",
        "cv_medium_plane_scout_airframe",
        "large_plane_airframe",
        "large_plane_awacs_airframe",
        "large_plane_cas_airframe",
        "large_plane_air_transport_airframe",
        "large_plane_maritime_patrol_airframe",
    ]
    for idx, line_type in enumerate(line_types):
        if line_type == item[0:len(line_type)]:
            # print(item[len(line_type) + 1])
            val += idx * factor + int(item[len(line_type) + 1]) - output_range[0]
    return val

# generate_air()

# what the fuck is this and why am i writing this instead of copying from SO or some ai hivemind?!
def get_roman_numeral(num):
    julius_caesar = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CM",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        3: "III",
        2: "II",
        1: "I",
    }
    temp = num
    result = ""
    for k, v in julius_caesar.items():
        while temp >= k:
            temp -= k
            result += v
    return result
    
equipment_name_guide = {
    "country": "SIA",
    "use_country_as_prefix": True,
    "randomize_use_dash": True,
    "eq_types": {
        "anti_tank": {
            "type_prefix": "Anti_tank_",
            "count": [5, 11],
            "prefix": "SIAT",
            "suffix": "",
            "use_roman_numeral": False,
            "use_country_as_prefix": False,
            "use_dash": False,
            "no_space": False
            },
        "heavy_anti_tank": {
            "type_prefix": "Heavy_Anti_tank_",
            "count": [5, 11],
            "prefix": "MGFART",
            "suffix": "",
            "use_roman_numeral": False,
            "use_country_as_prefix": False,
            "use_dash": True,
            "no_space": False
            },
        "artillery": {
            "type_prefix": "artillery_",
            "count": [5, 11],
            "prefix": "DT",
            "suffix": "",
            "use_roman_numeral": False,
            "use_country_as_prefix": False,
            "use_dash": True,  
            "no_space": False
            },
        "anti_air": {
            "type_prefix": "Anti_air_",
            "count": [5, 11],
            "prefix": "RAA",
            "suffix": "",
            "use_roman_numeral": False,
            "use_country_as_prefix": False,
            "use_dash": True,
            "no_space": False
            },
        "transport_helicopter": {
            "type_prefix": "transport_helicopter",
            "count": [6, 10],
            "prefix": "Pĕd Bin H", # "Flying duck" :)
            "suffix": "",
            "use_roman_numeral": True,
            "use_country_as_prefix": False,
            "use_dash": True,
            "no_space": False
            },
        "infantry_weapons": {
            "type_prefix": "infantry_weapons",
            "count": [8, 14],
            "prefix": "Type",
            "suffix": "RTA",
            "use_roman_numeral" :False,
            "use_country_as_prefix": False,
            "use_dash": False,
            "no_space": False
            },
        "command_control": {
            "type_prefix": "command_control_equipment",
            "count": [7, 13],
            "prefix": "SIRTA",
            "suffix": "",
            "use_roman_numeral" : False,
            "use_country_as_prefix": False,
            "use_dash": True,
            "no_space": False
            },
        "util_vehicle": {
            "type_prefix": "util_vehicle",
            "count": [8, 14],
            "prefix": "Thairung MUV4",
            "suffix": "",
            "use_roman_numeral": False,
            "use_country_as_prefix": False,
            "use_dash": False,
            "no_space": True
            },
    }
}

def generate_equipment():
    output = []
    for eq in equipment_name_guide['eq_types'].values():
        prev_model_num = random.randint(0, 100) if eq['use_roman_numeral'] is False else random.randint(0, 5)
        use_dash = eq['use_dash'] if eq['use_dash'] is not None else False
        use_country_as_prefix = equipment_name_guide['use_country_as_prefix']
        if eq['use_country_as_prefix'] is not None and eq['use_country_as_prefix'] != use_country_as_prefix:
            use_country_as_prefix = eq['use_country_as_prefix']
        if equipment_name_guide['randomize_use_dash'] and eq['use_dash'] is None:
            random_num = random.randint(1, 100)
            if random_num >= 50:
                use_dash = True
        eq_prefix = f"{equipment_name_guide['country'][:2]}{eq['prefix']}" if use_country_as_prefix else eq['prefix']
        for i in range(eq['count'][0], eq['count'][1] + 1):
            model_num = random.randint(prev_model_num + 1, prev_model_num + 15)
            out = eq['type_prefix'] + str(i)
            if use_dash:
                out += f": \"{eq_prefix}-"
            else:
                out += f": \"{eq_prefix}" if eq['no_space'] is True else f": \"{eq_prefix} "
            if eq['use_roman_numeral'] is True:
                model_num = prev_model_num + 1
                out += get_roman_numeral(model_num) # only increment by 1 if roman numeral
            else:
                out += str(model_num)
            out += f" {eq['suffix']}\"" if len(eq['suffix']) > 0 else '"'
            output.append(out)
            prev_model_num = model_num
    # return output
    with open(f"output.txt", 'w') as f:
        for _i, line in enumerate(output):
            out = f"{equipment_name_guide['country']}_"+line
            out += "\n" if _i != len(output)-1 else ""
            f.write(out)

generate_equipment()

    