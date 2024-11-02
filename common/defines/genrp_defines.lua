NDefines.NDiplomacy.IDEOLOGY_JOIN_FACTION_MIN_LEVEL = 0.0			-- 0.3, ideology limit required to join faction
NDefines.NDiplomacy.PEACE_SCORE_PER_PASS = 0.5						-- 0.2, When you pass in a peace deal you gain this percent of your original score
NDefines.NGame.EVENT_TIMEOUT_DEFAULT = 20							-- 13, Default days before an event times out if not scripted

-- Embargo
NDefines.NTrade.BASE_TRADE_FACTOR = 50
NDefines.NTrade.PARTY_SUPPORT_TRADE_FACTOR = 20


-- Letter
NDefines.NGame.MAX_SCRIPTED_LOC_RECURSION = 1001				-- max recursion for scripted localizations


-- Division/Ship Editing
NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 0 				--Base cost to unlock a regiment slot,
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 0				--Base cost to change a regiment column.
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 0 					--Base cost to unlock a support slot

NDefines.NProduction.EQUIPMENT_MODULE_ADD_XP_COST = 0.0					-- XP cost for adding a new equipment module in an empty slot when creating an equipment variant.
NDefines.NProduction.EQUIPMENT_MODULE_REPLACE_XP_COST = 0.0				-- XP cost for replacing one equipment module with an unrelated module when creating an equipment variant.
NDefines.NProduction.EQUIPMENT_MODULE_CONVERT_XP_COST = 0.0				-- XP cost for converting one equipment module to a related module when creating an equipment variant.
NDefines.NProduction.EQUIPMENT_MODULE_REMOVE_XP_COST = 0.0				-- XP cost for removing an equipment module and leaving the slot empty when creating an equipment variant.


-- MP Optimisation
NDefines.NGame.GAME_SPEED_SECONDS = { 600.0, 0.5, 0.3, 0.2, 0.15 }
NDefines.NCountry.EVENT_PROCESS_OFFSET = 30
	NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 10
	NDefines_Graphics.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE = 200
	NDefines_Graphics.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE_STRATEGIC = 0