# Can't write anything smarter or better because I'm stupid as fuck and lazy as fuck

art_small_gun = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "art_small_gun_gen",
    "abbrev_prefix": "asg",
    "category": "art_small_gun_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "allowed_module_categories": "allowed_module_categories = { conversion_type_slot = { small_gun_conversion_type } special_type_slot_1 = { small_gun_ammo_module } special_type_slot_2 = { small_gun_ammo_module } special_type_slot_3 = { small_gun_ammo_module } }",
    "can_convert_from": [
        ["art_small_gun_module", 1.25],
        ["art_medium_gun_module", 1.25],
        ["art_big_gun_module", 1.25],
        ["art_small_rocket_module", 1.25],
        ["art_medium_rocket_module", 1.25],
        ["art_big_rocket_module", 1.25],
    ],
    "build_cost_resources": [
        ["steel", 1, 1],
        ["tungsten", 1],
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 45, 8, 0],
        ["hard_attack", 6.5, 1.125, 0],
        ["ap_attack", 21, 3.375, 0],
        ["build_cost_ic", 4, 0.75, 0],
        ["maximum_speed", -2.5, -0.375, 0],
        ["reliability", -0.22, -0.0425, 0],
        ["breakthrough", 12, 1.875, 0],
        ["defense", 18, 2.625, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
art_med_gun = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "art_med_gun_gen",
    "abbrev_prefix": "amg",
    "category": "art_med_gun_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "allowed_module_categories": "allowed_module_categories = { conversion_type_slot = { medium_gun_conversion_type } special_type_slot_1 = { medium_gun_ammo_module medium_gun_feature_module } special_type_slot_2 = { medium_gun_ammo_module medium_gun_feature_module } special_type_slot_3 = { medium_gun_ammo_module medium_gun_feature_module } }",
    "can_convert_from": [
        ["art_small_gun_module", 6],
        ["art_medium_gun_module", 6],
        ["art_big_gun_module", 6],
        ["art_small_rocket_module", 6],
        ["art_medium_rocket_module", 6],
        ["art_big_rocket_module", 6],
    ],
    "build_cost_resources": [
        ["steel", 2, 1],
        ["tungsten", 2],
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 60, 10.75, 0],
        ["hard_attack", 8.5, 1.5, 1, 0],
        ["ap_attack", 28, 4.5, 0],
        ["build_cost_ic", 5.5, 1, 0],
        ["maximum_speed", -3.25, -0.4375, 0],
        ["reliability", -0.22, -0.0425, 0],
        ["breakthrough", 8, 1.25, 0],
        ["defense", 12, 1.75, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
art_big_gun = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "art_big_gun_gen",
    "abbrev_prefix": "abg",
    "category": "art_big_gun_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "allowed_module_categories": "allowed_module_categories = { conversion_type_slot = { big_gun_conversion_type } special_type_slot_1 = { big_gun_ammo_module } special_type_slot_2 = { big_gun_ammo_module } special_type_slot_3 = { big_gun_ammo_module } }",
    "can_convert_from": [
        ["art_small_gun_module", 7.5],
        ["art_medium_gun_module", 7.5],
        ["art_big_gun_module", 7.5],
        ["art_small_rocket_module", 7.5],
        ["art_medium_rocket_module", 7.5],
        ["art_big_rocket_module", 7.5],
    ],
    "build_cost_resources": [
        ["steel", 2, 1],
        ["tungsten", 1],
        ["chromium", 2]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 75, 13.5, 0],
        ["hard_attack", 10.5, 1.8, 0],
        ["ap_attack", 28, 4.5, 0],
        ["build_cost_ic", 7, 1.25, 0],
        ["maximum_speed", -4, -0.625, 0],
        ["reliability", -0.22, -0.0425, 0],
        ["breakthrough", 4, 0.5, 0],
        ["defense", 6, 0.75, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
art_small_rocket = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "art_small_rocket_gen",
    "abbrev_prefix": "asr",
    "category": "art_small_rocket_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "allowed_module_categories": "allowed_module_categories = { conversion_type_slot = { small_rocket_conversion_type } special_type_slot_1 = { small_rocket_ammo_module } special_type_slot_2 = { small_rocket_ammo_module } special_type_slot_3 = { small_rocket_ammo_module } }",
    "can_convert_from": [
        ["art_small_gun_module", 5],
        ["art_medium_gun_module", 5],
        ["art_big_gun_module", 5],
        ["art_small_rocket_module", 5],
        ["art_medium_rocket_module", 5],
        ["art_big_rocket_module", 5],
    ],
    "build_cost_resources": [
        ["steel", 1, 1],
        ["tungsten", 1],
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 49, 8.5, 0],
        ["hard_attack", 4.25, 0.8125, 0],
        ["ap_attack", 11, 1.75, 0],
        ["build_cost_ic", 5, 0.8125, 0],
        ["maximum_speed", -2.8, -0.45, 0],
        ["reliability", -0.22, -0.0425, 0],
        ["breakthrough", 11, 1.25, 0],
        ["defense", 11, 1.25, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
art_med_rocket = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "art_med_rocket_gen",
    "abbrev_prefix": "amr",
    "category": "art_med_rocket_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "allowed_module_categories": "allowed_module_categories = { conversion_type_slot = { medium_rocket_conversion_type } special_type_slot_1 = { medium_rocket_ammo_module } special_type_slot_2 = { medium_rocket_ammo_module } special_type_slot_3 = { medium_rocket_ammo_module } }",
    "can_convert_from": [
        ["art_small_gun_module", 6],
        ["art_medium_gun_module", 6],
        ["art_big_gun_module", 6],
        ["art_small_rocket_module", 6],
        ["art_medium_rocket_module", 6],
        ["art_big_rocket_module", 6],
    ],
    "build_cost_resources": [
        ["steel", 1, 1],
        ["tungsten", 1],
        ["aluminium", 1]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 65, 11.5, 0],
        ["hard_attack", 5.5, 1, 0],
        ["ap_attack", 11, 1.5, 0],
        ["build_cost_ic", 6.4, 1.1, 0],
        ["maximum_speed", -3.25, -0.4375, 0],
        ["reliability", -0.22, -0.0425, 0],
        ["breakthrough", 11, 1.75, 0],
        ["defense", 11, 1.75, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
art_big_rocket = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "art_big_rocket_gen",
    "abbrev_prefix": "abr",
    "category": "art_big_rocket_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "allowed_module_categories": "allowed_module_categories = { special_type_slot_1 = { big_rocket_ammo_module } special_type_slot_2 = { big_rocket_ammo_module } special_type_slot_3 = { big_rocket_ammo_module } }",
    "can_convert_from": [
        ["art_small_gun_module", 7],
        ["art_medium_gun_module", 7],
        ["art_big_gun_module", 7],
        ["art_small_rocket_module", 7],
        ["art_medium_rocket_module", 7],
        ["art_big_rocket_module", 7],
    ],
    "build_cost_resources": [
        ["steel", 2, 1],
        ["tungsten", 1],
        ["aluminium", 1]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 80, 14.25, 0],
        ["hard_attack", 7, 1.25, 0],
        ["ap_attack", 11, 1.5, 0],
        ["build_cost_ic", 7, 1.2, 0],
        ["maximum_speed", -3.5, -0.5, 0],
        ["reliability", -0.22, -0.0425, 0],
        ["breakthrough", 5.5, 0.875, 0],
        ["defense", 5.5, 0.875, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
helicopter_rocket_pod = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "helicopter_rocket_pod_gen",
    "abbrev_prefix": "hrg",
    "category": "helicopter_rockets_type",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["helicopter_atgm_type", 1.35],
        ["helicopter_rockets_type", 1.35],
    ],
    "build_cost_resources": [
        ["aluminium", 1, 1]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 3.6, 0.4, 0],
        ["soft_attack", 27, 3, 0],
        ["reliability", -0.05, 0, 0],
        ["maximum_speed", -2.4, -0.3, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
helicopter_atgm = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "helicopter_atgm_gen",
    "abbrev_prefix": "hag",
    "category": "helicopter_atgm_type",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["helicopter_atgm_type", 2],
        ["helicopter_rockets_type", 2],
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 8, 1, 0],
        ["soft_attack", 20, 2.5, 0],
        ["reliability", -0.05, 0, 0],
        ["maximum_speed", -2.4, -0.3, 0],
    ],
    "add_average_stats": [
        ["ap_attack", 45, 5, 0]
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
helicopter_multiple_atgm = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "helicopter_multiple_atgm_gen",
    "abbrev_prefix": "hmag",
    "category": "helicopter_multiple_atgm_type",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["helicopter_multiple_atgm_type", 8],
    ],
    "build_cost_resources": [
        ["tungsten", 1, 1]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 16, 2, 0],
        ["soft_attack", 40, 5, 0],
        ["reliability", -0.2, 0, 0],
        ["maximum_speed", -8, -1, 0],
    ],
    "add_average_stats": [
        ["ap_attack", 80, 10, 0]
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
smoothbore_atgm = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "smoothbore_atgm_gen",
    "abbrev_prefix": "satgm",
    "category": "tank_atgm_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["tank_atgm_module", 2.05],
    ],
    "build_cost_resources": [
        ["tungsten", 2, 1]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 1.8, 0.2, 0],
        ["hard_attack", 9.5, 1.375, 0],
        ["ap_attack", 24, 3, 0],
        ["reliability", -0.05, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
afv_atgm = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "afv_atgm_gen",
    "abbrev_prefix": "aag",
    "category": "afv_atgm_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["tank_atgm_module", 2.05],
    ],
    "build_cost_resources": [
        ["tungsten", 2, 1]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 1.6, 0.2, 0],
        ["hard_attack", 9.5, 1.375, 0],
        ["ap_attack", 24, 3, 0],
        ["reliability", -0.13, -0.02, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
helicopter_heavy_atgm = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "helicopter_heavy_atgm_gen",
    "abbrev_prefix": "hag",
    "category": "helicopter_heavy_atgm_type",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["helicopter_heavy_atgm_type", 8],
    ],
    "build_cost_resources": [
        ["tungsten", 2, 1]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 16, 2, 0],
        ["hard_attack", 32, 4, 0],
        ["reliability", -0.25, 0, 0],
        ["maximum_speed", -12, -1.5, 0],
    ],
    "add_average_stats": [
        ["ap_attack", 200, 25, 0]  
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
aa_launchers = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "aa_launchers_gen",
    "abbrev_prefix": "aal",
    "category": "tank_aa_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["tank_aa_module", 1.8],
    ],
    "build_cost_resources": [
        ["chromium", 2, 0],
        ["tungsten", 2, 1]
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 1.6, 0.2875, 0],
        ["air_attack", 2.0, 0.25, 0],
        ["maximum_speed", -1, -0.125, 0],
        ["reliability", -0.05, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_support_missile_system = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_support_missile_system_",
    "abbrev_prefix": "spaam",
    "category": "spaa_support_missile_system_category",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["tank_aa_module", 1.8],
    ],
    "build_cost_resources": [
        ["chromium", 1, 1],
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["hard_attack", 3, 0.375, 0],
        ["ap_attack", 12, 1.5, 0],
        ["air_attack", 6, 0.75, 0],
        ["build_cost_ic", 4, 0.5, 0],
        ["maximum_speed", -1.5, 0, 0],
        ["reliability", -0.075, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_auxiliary_autocannon = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_auxiliary_autocannon_",
    "abbrev_prefix": "sas",
    "category": "spaa_auxiliary_autocannon_category",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["tank_aa_module", 1.8],
    # ],
    # "build_cost_resources": [
    #     ["chromium", 1, 1],
    # ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 4, 0.5, 0],
        ["air_attack", 3, 0.375, 0],
        ["build_cost_ic", 1.35, 0.15, 0],
        ["maximum_speed", -0.5, 0, 0],
        ["reliability", -0.05, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_auxiliary_heavy_autocannon = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_auxiliary_heavy_autocannon_",
    "abbrev_prefix": "saha",
    "category": "spaa_auxiliary_autocannon_category",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["tank_aa_module", 1.8],
    # ],
    "build_cost_resources": [
        ["steel", 1, 1],
    ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 8, 1, 0],
        ["hard_attack", 2, 0.25, 0],
        ["air_attack", 6, 0.75, 0],
        ["build_cost_ic", 2, 0.25, 0],
        ["maximum_speed", -1, 0, 0],
        ["reliability", -0.1, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_battlestation = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_battlestation_gen",
    "abbrev_prefix": "sab",
    "category": "spaa_battlestation_modules",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "can_convert_from": [
        ["spaa_battlestation_modules", 1.25],
    ],
    # "build_cost_resources": [
    #     ["steel", 1, 1],
    # ],
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 2, 0.25, 0],
    ],
    "multiply_stats": [
        ["soft_attack", 0.15, 0.025, 0],
        ["hard_attack", 0.15, 0.025, 0],
        ["breakthrough", 0.15, 0.025, 0],
        ["defense", 0.15, 0.025, 0],
        ["air_attack", 0.15, 0.025, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_light_autocannon = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_light_autocannon",
    "abbrev_prefix": "smg",
    "category": "spaa_light_autocannon_systems",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    # "build_cost_resources": [
    #     ["steel", 1, 1],
    # ],
    "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_support_missile_system_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 8, 1, 0],
        ["air_attack", 4, 0.5, 0],
        ["build_cost_ic", 5, 1, 0],
        ["maximum_speed", -1, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_autocannon = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_autocannon_",
    "abbrev_prefix": "sa",
    "category": "spaa_autocannon_systems",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    "build_cost_resources": [
        ["tungsten", 1, 1],
    ],
    "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_support_missile_system_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["soft_attack", 10, 1.25, 0],
        ["hard_attack", 2, 0.25, 0],
        ["air_attack", 7.5, 0.9375, 0],
        ["build_cost_ic", 3, 0.375, 0],
        ["maximum_speed", -2, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_missiles = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_missiles_",
    "abbrev_prefix": "sm",
    "category": "spaa_missile_systems",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    "build_cost_resources": [
        ["chromium", 1, 1],
        ["tungsten", 1, 0],
    ],
    "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["hard_attack", 6, 0.75, 0],
        ["ap_attack", 36, 4.5, 0],
        ["air_attack", 12, 1.5, 0],
        ["build_cost_ic", 8, 1, 0],
        ["maximum_speed", -3, 0, 0],
    ],
    "multiply_stats": [
        ["breakthrough", -0.03, 0.03, 0],
        ["defense", -0.03, 0.03, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_short_range_missiles = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_short_range_missiles_",
    "abbrev_prefix": "ssrm",
    "category": "spaa_short_range_missile_systems",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    "build_cost_resources": [
        ["chromium", 1, 1],
    ],
    "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["air_attack", 12, 1.5, 0],
        ["build_cost_ic", 6, 0.75, 0],
        ["maximum_speed", -3, 0, 0],
    ],
    "multiply_stats": [
        ["breakthrough", -0.03, 0.03, 0],
        ["defense", -0.03, 0.03, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_long_range_missiles = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_long_range_missiles_",
    "abbrev_prefix": "slrm",
    "category": "spaa_long_range_missile_systems",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    "build_cost_resources": [
        ["chromium", 2, 1],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["air_attack", 21.5, 2.5, 0],
        ["build_cost_ic", 12, 1.5, 0],
        ["maximum_speed", -4.5, 0, 0],
        ["reliability", -0.2, 0.025, 0],
    ],
    "multiply_stats": [
        ["breakthrough", -0.2, 0.025, 0],
        ["defense", -0.2, 0.025, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_chassis_truck = {
    "start_idx": 5,
    "end_idx": 11,
    "name_prefix": "spaa_chassis_truck_gen",
    "abbrev_prefix": "sct",
    "category": "spaa_chassis_truck_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    "build_cost_resources": [
        ["rubber", 1, 0],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 1, 0.125, 0],
        ["defense", 4, 0.5, 0],
        ["breakthrough", 2, 0.25, 0],
    ],
    "multiply_stats": [
        ["hardness", -0.8, 0, 0],
        ["maximum_speed", 0.15, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_chassis_afv = {
    "start_idx": 5,
    "end_idx": 11,
    "name_prefix": "spaa_chassis_afv_gen",
    "abbrev_prefix": "sca",
    "category": "spaa_chassis_afv_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    "build_cost_resources": [
        ["aluminium", 2, 0],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["armor_value", 16, 2, 0],
        ["build_cost_ic", 3.2, 0.4, 0],
        ["defense", 8, 1, 0],
        ["breakthrough", 8, 1, 0],
        ["maximum_speed", -1.5, 0, 0],
    ],
    # "multiply_stats": [
    #     ["hardness", -0.8, 0, 0],
    #     ["maximum_speed", 0.15, 0, 0],
    # ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_chassis_tank = {
    "start_idx": 5,
    "end_idx": 11,
    "name_prefix": "spaa_chassis_tank_gen",
    "abbrev_prefix": "scta",
    "category": "spaa_chassis_tank_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    "build_cost_resources": [
        ["steel", 3, 0],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["armor_value", 80, 10, 0],
        ["build_cost_ic", 8, 1, 0],
        ["defense", 24, 3, 0],
        ["breakthrough", 32, 4, 0],
        ["maximum_speed", -3, 0, 0],
    ],
    "multiply_stats": [
        ["hardness", 0.5, 0, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
spaa_optical_guidance = {
    "start_idx": 6,
    "end_idx": 12,
    "name_prefix": "spaa_optical_guidance_gen",
    "abbrev_prefix": "spog",
    "category": "spaa_optical_guidance_systems",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "can_convert_from": [
    #     ["spaa_battlestation_modules", 1.25],
    # ],
    "build_cost_resources": [
        ["aluminium", 1, 0],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["build_cost_ic", 2, 0.25, 0],
    ],
    "multiply_stats": [
        ["air_attack", 0.4, 0.05, 0],
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
avionics_drone = {
    "start_idx": 5,
    "end_idx": 8,
    "name_prefix": "avionics_drone_",
    "abbrev_prefix": "avd",
    "category": "plane_drone_systems",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 4,
    "add_equipment_type": "suicide",
    "can_convert_from": [
        ["plane_drone_systems", 55],
    ],
    "build_cost_resources": [
        ["chromium", 2, 0],
        ["tungsten", 3, 1],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["weight", 36, 4, 0],
		["night_penalty", -0.24, -0.12, 0],
    ],
    "multiply_stats": [
        ["air_defence", -0.15, 0.05, 0],
		["air_attack", 0.05, 0.1, 0],
		["build_cost_ic", -0.2, -0.017, 0],
		["air_superiority", 0.1, 0.2, 0],
    ],
    "manpower": [-15, -3],
    "allow_mission_type": [
        "recon",
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
avionics_manned = {
    "start_idx": 5,
    "end_idx": 8,
    "name_prefix": "avionics_manned_",
    "abbrev_prefix": "avm",
    "category": "plane_avionics",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 2,
    # "add_equipment_type": "suicide",
    "can_convert_from": [
        ["plane_avionics", 18],
    ],
    "build_cost_resources": [
        ["tungsten", 3, 1],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
		["air_defence", 36, 6, 0],
		["naval_strike_targetting", 3.5, 0.83, 0],
		["build_cost_ic", 23, 6, 0],
		["weight", 9, 2, 0],
		["night_penalty", -0.26, -0.07, 0],
    ],
    "multiply_stats": [
		["air_superiority", 0.15, 0.05, 0],
		["air_attack", 0.2, 0.05, 0],
		["air_agility", 0.18, 0.05, 0],
		["air_defence", 0.08, 0.02, 0],
		["air_ground_attack", 0.2, 0.05, 0],
		["air_bombing", 0.2, 0.05, 0],
    ],
    "manpower": [-1, 0],
    # "allow_mission_type": [
    #     "recon",
    # ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
em_lock_detection_system = {
    "start_idx": 4,
    "end_idx": 7,
    "name_prefix": "em_lock_detection_system_gen",
    "abbrev_prefix": "elds",
    "category": "helicopter_em_lock_type",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    # "add_equipment_type": "suicide",
    # "can_convert_from": [
    #     ["plane_avionics", 18],
    # ],
    "build_cost_resources": [
        ["chromium", 1, 0],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
		["build_cost_ic", 3, 0.5, 0],
		["defense", 5, 1, 0],
		["breakthrough", 5, 1, 0],
		["reliability", 0.25, 0.05, 0],
    ],
    # "multiply_stats": [
	# 	["air_superiority", 0.15, 0.05, 0],
	# 	["air_attack", 0.2, 0.05, 0],
	# 	["air_agility", 0.18, 0.05, 0],
	# 	["air_defence", 0.08, 0.02, 0],
	# 	["air_ground_attack", 0.2, 0.05, 0],
	# 	["air_bombing", 0.2, 0.05, 0],
    # ],
    # "manpower": [-1, 0],
    # "allow_mission_type": [
    #     "recon",
    # ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
weap_buff_awacs = {
    "start_idx": 4,
    "end_idx": 7,
    "name_prefix": "weap_buff_awacs_",
    "abbrev_prefix": "awacs",
    "category": "plane_awacs_module",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 3,
    "add_equipment_type": "scout_plane",
    "forbid_equipment_type_exact_match_for_category": "forbid_equipment_type_exact_match_for_category = { plane_fighter_weapons = scout_plane plane_intercept_weapons = scout_plane plane_heavy_nav_weapons = scout_plane plane_cas_weapons = scout_plane plane_nav_weapons = scout_plane plane_guided_bombs = scout_plane plane_heavy_modules = scout_plane plane_unguided_bombs = scout_plane plane_multipurpose_gun = scout_plane plane_multipurpose_pod = scout_plane plane_bomb_bay = scout_plane }",
    # "can_convert_from": [
    #     ["plane_avionics", 18],
    # ],
    "build_cost_resources": [
        ["tungsten", 1, 0],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["air_superiority", 54, 11, 0],
		["build_cost_ic", 132.5, 32.5, 0],
		["weight", 23, 3.5, 0],
    ],
    "multiply_stats": [
        ["air_agility", -0.5, 0.2, 0],
		["air_range", -0.02, 0.03, 0],
		["maximum_speed", -0.09, 0.025, 0],
    ],
    # "manpower": [-1, 0],
    "allow_mission_type": [
        "recon",
		"naval_patrol",
    ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}
engine_light_single = {
    "start_idx": 6,
    "end_idx": 8,
    "name_prefix": "engine_light_single_",
    "abbrev_prefix": "je1",
    "category": "plane_light_single",
    "sfx": "sfx_ui_sd_module_turret",
    "xp_cost": 2,
    # "add_equipment_type": "scout_plane",
    # "forbid_equipment_type_exact_match_for_category": "forbid_equipment_type_exact_match_for_category = { plane_fighter_weapons = scout_plane plane_intercept_weapons = scout_plane plane_heavy_nav_weapons = scout_plane plane_cas_weapons = scout_plane plane_nav_weapons = scout_plane plane_guided_bombs = scout_plane plane_heavy_modules = scout_plane plane_unguided_bombs = scout_plane plane_multipurpose_gun = scout_plane plane_multipurpose_pod = scout_plane plane_bomb_bay = scout_plane }",
    "can_convert_from": [
        ["engine_light_single_4", 19],
    ],
    "build_cost_resources": [
        ["chromium", 1, 0.5],
    ],
    # "allowed_module_categories": "allowed_module_categories = { spaa_secondary_armament = { spaa_auxiliary_autocannon_category } }",
    "add_stats": [
        # item, base, increment, advance_increment
        ["maximum_speed", 1653, 109.5, 0],
        ["thrust", 99, 15.75, 0],
        ["build_cost_ic", 67, 8, 0],
        ["fuel_consumption", 4, -0.1, 0],
    ],
    # "multiply_stats": [
    #     ["air_agility", -0.5, 0.2, 0],
	# 	["air_range", -0.02, 0.03, 0],
	# 	["maximum_speed", -0.09, 0.025, 0],
    # ],
    # "manpower": [-1, 0],
    # "allow_mission_type": [
    #     "recon",
	# 	"naval_patrol",
    # ],
    "generation_options": {
        "advances": 2,
        "advance_at_start": False
    }
}

def get_add_stats(add_stats, generation, advance_generation):
    result = []
    for item in add_stats:
        val = round(item[1] + item[2] + item[3] * advance_generation, 4)
        result.append([item[0], val, item[2], item[3]])
    return result

def get_add_stats_string(add_stats, type = "add_stats"):
    result = "\tadd_stats = {\n" if type == "add_stats" else "\tmultiply_stats = {\n" if type == "multiply_stats" else "\tadd_average_stats = {\n"
    for item in add_stats:
        stat_name = item[0]
        val = item[1]
        stat = f"\t\t{stat_name} = {val}\n"
        result += stat
    result += "\t}\n"
    return result

def get_can_convert_from(can_convert_from):
    result = ""
    for item in can_convert_from:
        result += "\tcan_convert_from = { " + f"module_category = {item[0]} convert_cost_ic = {item[1]}" + " }\n"
    return result

def get_build_cost_resources(build_cost_resources, advance_generation):
    result = "\tbuild_cost_resources = {"
    for item in build_cost_resources:
        resource = item[0]
        amount = item[1]
        if len(item) > 2:
            amount += item[2] * advance_generation
        result += f" {resource} = {amount}"
    return result + " }\n"

def get_allow_mission_type(types):
    result = "\tallow_mission_type = { "
    for type in types:
        result += f"{type} "
    return result + "}\n"

def get_manpower(manpower, generation):
    return f"\tmanpower = {manpower[0] + manpower[1] * generation}\n"

def generate(values):
    content = ""
    start = values['start_idx']
    end = values['end_idx']
    advance_generation = 0
    advance_num = values['generation_options']['advances']
    advance_at_start = values['generation_options']['advance_at_start']
    generations_to_advance = []
    count = start
    advance_diff = (end - start) / advance_num
    # print(advance_diff)
    if advance_at_start and advance_num >= 1:
        advance_generation = 1
        generations_to_advance.append(start)
        # count += advance_diff
    while (count < end and len(generations_to_advance) < advance_num):
        # print(count)
        count += round(advance_diff)
        generations_to_advance.append(min(count, end))
        # print("generations to advance:", generations_to_advance)
    prev_add_stats = values['add_stats'] if 'add_stats' in values else None
    prev_multiply_stats = values['multiply_stats'] if 'multiply_stats' in values else None
    prev_add_average_stats = values['add_average_stats'] if 'add_average_stats' in values else None
    for idx in range(values['start_idx'], values['end_idx'] + 1):
        # print(prev_add_stats)
        if idx != start and idx in generations_to_advance:
            advance_generation += 1
            advance_generation = min(advance_num, advance_generation)
        content += f"\n{values['name_prefix']}{idx}" + " = {\n"
        abbrev = f"\tabbreviation = \"{values['abbrev_prefix']}{idx}\"\n"
        category = f"\tcategory = {values['category']}\n"
        sfx = f"\tsfx = {values['sfx']}\n"
        parent = f"\tparent = {values['name_prefix']}{idx-1}\n"
        add_equipment_type = f"\tadd_equipment_type = {values['add_equipment_type']}\n" if 'add_equipment_type' in values else ""
        forbid_equipment_type_exact_match_for_category = f"\t{values['forbid_equipment_type_exact_match_for_category']}\n" if 'forbid_equipment_type_exact_match_for_category' in values else ""
        allowed_module_categories = f"\t{values['allowed_module_categories']}\n" if 'allowed_module_categories' in values else ""
        prev_add_stats = get_add_stats(prev_add_stats, idx-start+1, advance_generation) if 'add_stats' in values else None
        add_stats = get_add_stats_string(prev_add_stats) if prev_add_stats else ""
        prev_multiply_stats = get_add_stats(prev_multiply_stats, idx-start+1, advance_generation) if 'multiply_stats' in values else None
        multiply_stats = get_add_stats_string(prev_multiply_stats, "multiply_stats") if prev_multiply_stats else ""
        prev_add_average_stats = get_add_stats(prev_add_average_stats, idx-start+1, advance_generation) if 'add_average_stats' in values else None
        add_average_stats = get_add_stats_string(prev_add_average_stats, "add_average_stats") if prev_add_average_stats else ""
        manpower = get_manpower(values['manpower'], idx-start+1) if 'manpower' in values else ""
        xp_cost = f"\txp_cost = {values['xp_cost']}\n"
        can_convert_from = get_can_convert_from(values['can_convert_from']) if 'can_convert_from' in values else ""
        build_cost_resources = get_build_cost_resources(values['build_cost_resources'], advance_generation) if 'build_cost_resources' in values else ""
        allow_mission_type = get_allow_mission_type(values['allow_mission_type']) if 'allow_mission_type' in values else ""
        content += abbrev + category + sfx + parent + add_equipment_type + forbid_equipment_type_exact_match_for_category + allowed_module_categories + add_stats + multiply_stats + add_average_stats + manpower + xp_cost + can_convert_from + build_cost_resources + allow_mission_type + "}"
    return content

def create(values):
    contents = []
    for value in values:
        contents.append(generate(value))
    with open('modules_generated.txt', 'w') as f:
        for content in contents:
            f.write(content)
    
artillery_folder_modules = [
    art_small_gun,
    art_med_gun,
    art_big_gun,
    art_small_rocket, 
    art_med_rocket,
    art_big_rocket,
    helicopter_rocket_pod,
    helicopter_atgm, 
    helicopter_multiple_atgm,
    smoothbore_atgm,
    afv_atgm,
    helicopter_heavy_atgm,
    aa_launchers,
    spaa_support_missile_system,
    spaa_auxiliary_autocannon,
    spaa_auxiliary_heavy_autocannon,
    spaa_battlestation,
    spaa_light_autocannon,
    spaa_autocannon,
    spaa_missiles,
    spaa_short_range_missiles,
    spaa_long_range_missiles,
    spaa_chassis_truck,
    spaa_chassis_afv,
    spaa_chassis_tank,
    spaa_optical_guidance
]    
fixed_wing_folder_modules = [
    avionics_drone,
    avionics_manned,
    em_lock_detection_system,
    weap_buff_awacs,
    engine_light_single
]

create(fixed_wing_folder_modules)