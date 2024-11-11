-- ai
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_DOCTRINE = 10000       -- Increase interval to reduce calculations.
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_TEMPLATE = 10000       -- Increase interval to reduce calculations.
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_EQUIPMENT = 10000      -- Increase interval to reduce calculations.
NDefines.NAI.HOURS_BETWEEN_ENCIRCLEMENT_DISCOVERY = 24 -- Increase interval to reduce calculations.
NDefines.NAI.AI_UPDATE_ROLES_FREQUENCY_HOURS = 60000000     -- Increase interval to reduce calculations.
NDefines.NAI.UPDATE_SUPPLY_MOTORIZATION_FREQUENCY_HOURS = 60000000 -- Increase interval to reduce calculations.
NDefines.NAI.UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS = 336000 -- Increase interval to reduce calculations.
NDefines.NAI.RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE = 60       -- Increase interval to reduce calculations.
NDefines.NAI.MICRO_POCKET_SIZE = 0                          -- Keep as is for efficiency.
NDefines.NAI.DAYS_BETWEEN_AIR_PRIORITIES_UPDATE = 20000     -- Increase interval to reduce calculations.
NDefines.NAI.DIPLOMACY_RECALCULATE_INTERVAL = 2000          -- Increase interval to reduce calculations.
NDefines.NAI.PLAN_ACTIVATION_SUPERIORITY_AGGRO = 2.0        -- Keep as is.
NDefines.NAI.PLAN_VALUE_TO_EXECUTE = -1.0                   -- Keep as is.
NDefines.NAI.HOUR_BETWEEN_ENEMY_ARMY_CHECKS = 1           -- Increase interval to reduce calculations.
NDefines.NAI.MINIMUM_EQUIPMENT_TO_ASK_LEND_LEASE = 0.5      -- Keep as is.

NDefines.NTrade.ANTI_MONOPOLY_TRADE_FACTOR = 0              -- Keep as is.
NDefines.NTrade.RELATION_TRADE_FACTOR = 1                   -- Keep as is.
NDefines.NTrade.DISTANCE_TRADE_FACTOR = -0.02               -- Keep as is.
NDefines.NTrade.PARTY_SUPPORT_TRADE_FACTOR = 50             -- Keep as is.

-- QOL
NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 3                    -- Reduce combat log months to reduce save file size.
NDefines.NGame.MESSAGE_TIMEOUT_DAYS = 5                     -- Reduce message timeout days to clear messages faster.
NDefines.NGame.MISSION_REMOVE_FROM_INTERFACE_DEFAULT = 3    -- Keep as is.
-- NDefines.NGame.MAX_SCRIPTED_LOC_RECURSION = 20            -- Keep commented out.
-- Defines.NGame.MAX_EFFECT_ITERATION = 100                 -- Keep commented out.

NDefines.NCountry.EVENT_PROCESS_OFFSET = 120                -- Increase event process offset for better performance.
NDefines.NCountry.COUNTRY_SCORE_MULTIPLIER = 0.05           -- Reduce country score multiplier.
NDefines.NCountry.ARMY_SCORE_MULTIPLIER = 0.05              -- Reduce army score multiplier.
NDefines.NCountry.NAVY_SCORE_MULTIPLIER = 0.05              -- Reduce navy score multiplier.

-- Visibility of enemy divisions
NDefines.NMilitary.DIVISION_VISIBILITY = 100.0              -- Ensure divisions are visible.
NDefines.NMilitary.DIVISION_DETECTION_CHANCE = 100.0        -- Ensure divisions are detected.
NDefines.NMilitary.DIVISION_DETECTION_RADIUS = 1000.0       -- Increase detection radius.

-- Additional Optimizations
NDefines.NMilitary.ARMY_EXP_BASE_LEVEL = 0.1                -- Reduce base army experience gain.
NDefines.NMilitary.ARMY_EXP_GAIN = 0.05                     -- Reduce army experience gain.
NDefines.NMilitary.DIVISION_ORG_LOSS_FACTOR = 0.5           -- Reduce division organization loss.
NDefines.NMilitary.DIVISION_STRENGTH_LOSS_FACTOR = 0.5      -- Reduce division strength loss.
NDefines.NMilitary.COMMAND_POWER_GAIN = 0.05                -- Reduce command power gain.
NDefines.NMilitary.COMMAND_POWER_MAX = 100                  -- Set maximum command power.
NDefines.NMilitary.COMMAND_POWER_REGENERATION_RATE = 0.01   -- Reduce command power regeneration rate.
NDefines.NResistance.COMPLIANCE_GROWTH_BASE = 0.4              -- Increase base compliance growth.
NDefines.NCountry.FUEL_CAPACITY_DEFAULT_HOURS = 720         -- Set default fuel capacity in hours.
NDefines.NCountry.FUEL_GAIN_PER_OIL = 0.1                   -- Reduce fuel gain per oil.
NDefines.NCountry.FUEL_GAIN_PER_OIL_FROM_STATE = 0.1        -- Reduce fuel gain per oil from state.
NDefines.NCountry.FUEL_GAIN_PER_OIL_FROM_BUILDING = 0.1     -- Reduce fuel gain per oil from building.

NDefines.NSupply.SUPPLY_CACHE_CAPACITY = 100                -- Set supply cache capacity.
NDefines.NSupply.SUPPLY_CACHE_GAIN = 0.1                    -- Reduce supply cache gain.
NDefines.NSupply.SUPPLY_CACHE_CONSUMPTION = 0.1             -- Reduce supply cache consumption.

NDefines.NMarket.INTERNATIONAL_MARKET_BASE_FACTOR = 0.5     -- Reduce international market base factor.
NDefines.NMarket.INTERNATIONAL_MARKET_TRADE_FACTOR = 0.5    -- Reduce international market trade factor.
NDefines.NMarket.INTERNATIONAL_MARKET_RESOURCE_FACTOR = 0.5 -- Reduce international market resource factor.