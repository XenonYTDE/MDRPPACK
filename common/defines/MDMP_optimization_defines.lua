-- AI Optimization (NAI section - only affects AI)
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_DOCTRINE = 10000
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_TEMPLATE = 10000
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_EQUIPMENT = 10000
NDefines.NAI.HOURS_BETWEEN_ENCIRCLEMENT_DISCOVERY = 24
NDefines.NAI.AI_UPDATE_ROLES_FREQUENCY_HOURS = 60000000
NDefines.NAI.UPDATE_SUPPLY_MOTORIZATION_FREQUENCY_HOURS = 60000000
NDefines.NAI.UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS = 336000
NDefines.NAI.RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE = 60
NDefines.NAI.MICRO_POCKET_SIZE = 0
NDefines.NAI.DAYS_BETWEEN_AIR_PRIORITIES_UPDATE = 20000
NDefines.NAI.DIPLOMACY_RECALCULATE_INTERVAL = 2000
NDefines.NAI.PLAN_ACTIVATION_SUPERIORITY_AGGRO = 2.0
NDefines.NAI.PLAN_VALUE_TO_EXECUTE = -1.0
NDefines.NAI.HOUR_BETWEEN_ENEMY_ARMY_CHECKS = 1
NDefines.NAI.MINIMUM_EQUIPMENT_TO_ASK_LEND_LEASE = 0.5

-- AI Politics & Laws (only affects AI behavior)
NDefines.NAI.POLITICAL_IDEA_MIN_SCORE = 0.1                             -- NEW: Minimum score for AI to consider political ideas
NDefines.NAI.DIPLOMACY_IMPROVE_RELATION_COST_FACTOR = 100              -- NEW: AI less likely to spam improve relations
NDefines.NAI.DIPLOMACY_ACCEPT_VOLUNTEERS_BASE = 50                     -- NEW: Base value for AI accepting volunteers
NDefines.NAI.DIPLOMACY_ACCEPT_ATTACHE_BASE = 50                        -- NEW: Base value for AI accepting attaches
NDefines.NAI.MAX_AHEAD_RESEARCH_PENALTY = 1.5                         -- NEW: AI penalty for ahead of time research

-- Trade and Embargo Settings
NDefines.NTrade.ANTI_MONOPOLY_TRADE_FACTOR = 0
NDefines.NTrade.RELATION_TRADE_FACTOR = 1
NDefines.NTrade.DISTANCE_TRADE_FACTOR = -0.02
NDefines.NTrade.BASE_TRADE_FACTOR = 50                                -- NEW: Base trade factor increased
NDefines.NTrade.PARTY_SUPPORT_TRADE_FACTOR = 20                       -- NEW: Reduced from 50 for better balance

-- Game Performance and MP Optimization
NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 1000
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 100                              -- NEW: Increased from 60 for MP
NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 3
NDefines.NGame.MESSAGE_TIMEOUT_DAYS = 5
NDefines.NGame.GAME_SPEED_SECONDS = { 1.0, 0.25, 0.1, 0.05, 0.0 }   -- NEW: MP optimized speeds
NDefines.NGame.MISSION_REMOVE_FROM_INTERFACE_DEFAULT = 3
NDefines.NGame.EVENT_TIMEOUT_DEFAULT = 20                            -- NEW: Increased from 13
NDefines.NGame.MAX_SCRIPTED_LOC_RECURSION = 1001                    -- NEW: Increased for more complex scripts

-- Country Settings
NDefines.NCountry.EVENT_PROCESS_OFFSET = 30                         -- NEW: Reduced for better MP performance
NDefines.NCountry.COUNTRY_SCORE_MULTIPLIER = 0.05
NDefines.NCountry.ARMY_SCORE_MULTIPLIER = 0.05
NDefines.NCountry.NAVY_SCORE_MULTIPLIER = 0.05
NDefines.NCountry.POLITICAL_POWER_UPPER_CAP = 5000                 -- NEW: Increased PP cap
NDefines.NCountry.BASE_MAX_COMMAND_POWER = 500                     -- NEW: Increased command power cap
NDefines.NCountry.POPULATION_YEARLY_GROWTH_BASE = 0.01             -- NEW: Base population growth
NDefines.NCountry.FUEL_CAPACITY_DEFAULT_HOURS = 720
NDefines.NCountry.FUEL_GAIN_PER_OIL = 0.2
NDefines.NCountry.FUEL_GAIN_PER_OIL_FROM_STATE = 0.2
NDefines.NCountry.FUEL_GAIN_PER_OIL_FROM_BUILDING = 0.2

-- Military Settings
NDefines.NMilitary.DIVISION_VISIBILITY = 100.0
NDefines.NMilitary.DIVISION_DETECTION_CHANCE = 100.0
NDefines.NMilitary.DIVISION_DETECTION_RADIUS = 1000.0
NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 2500                    
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 2500                 
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 2500                      
NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 0        
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 0        
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 0          

-- Division/Ship Production
NDefines.NProduction.EQUIPMENT_MODULE_ADD_XP_COST = 0.0           -- NEW: Free equipment designing
NDefines.NProduction.EQUIPMENT_MODULE_REPLACE_XP_COST = 0.0       -- NEW: Free equipment designing
NDefines.NProduction.EQUIPMENT_MODULE_CONVERT_XP_COST = 0.0       -- NEW: Free equipment designing
NDefines.NProduction.EQUIPMENT_MODULE_REMOVE_XP_COST = 0.0        -- NEW: Free equipment designing

-- Politics & Laws
NDefines.NPolitics.BASE_POLITICAL_POWER_INCREASE = 2.75           -- NEW: Increased from 2.0
NDefines.NPolitics.ARMY_LEADER_COST = 25
NDefines.NPolitics.NAVY_LEADER_COST = 25

-- Diplomacy
NDefines.NDiplomacy.IDEOLOGY_JOIN_FACTION_MIN_LEVEL = 0.0        -- NEW: Removed ideology restrictions
NDefines.NDiplomacy.PEACE_SCORE_SCALE_FACTOR = 1.35             -- NEW: Better peace deals
NDefines.NDiplomacy.PEACE_SCORE_PER_PASS = 0.5                  -- NEW: Better peace deals

-- Market
NDefines.NMarket.MAX_CIV_FACTORIES_PER_CONTRACT = 15            -- NEW: Increased from default
NDefines.NMarket.INTERNATIONAL_MARKET_BASE_FACTOR = 0.75
NDefines.NMarket.INTERNATIONAL_MARKET_TRADE_FACTOR = 0.75
NDefines.NMarket.INTERNATIONAL_MARKET_RESOURCE_FACTOR = 0.75

-- Supply System
NDefines.NSupply.SUPPLY_CACHE_CAPACITY = 100
NDefines.NSupply.SUPPLY_CACHE_GAIN = 0.2
NDefines.NSupply.SUPPLY_CACHE_CONSUMPTION = 0.2

-- Graphics Optimization for MP
NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 10            -- NEW: MP optimization
NDefines_Graphics.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE = 200  -- NEW: MP optimization
NDefines_Graphics.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE_STRATEGIC = 0  -- NEW: MP optimization