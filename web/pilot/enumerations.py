ACTION_OR_ACTIVITY = [
    ("navigating with a pilot", "navigating with a pilot"), #1
    ("entering port", "entering port"), #2
    ("leaving port", "leaving port"), #3
    ("berthing", "berthing"), #4
    ("slipping", "slipping"), #5
    ("anchoring", "anchoring"), #6
    ("weighing anchor", "weighing anchor"), #7
    ("transiting", "transiting"), #8
    ("overtaking", "overtaking"), #9
    ("reporting", "reporting"), #10
    ("working cargo", "working cargo"), #11
    ("landing", "landing"), #12
    ("diving", "diving"), #13
    ("fishing", "fishing"), #14
    ("discharging overboard", "discharging overboard"), #15
    ("passing", "passing"), #16
]
CARDINAL_DIRECTION = [
    ("N", "N"), #1
    ("NNE", "NNE"), #2
    ("NE", "NE"), #3
    ("ENE", "ENE"), #4
    ("E", "E"), #5
    ("ESE", "ESE"), #6
    ("SE", "SE"), #7
    ("SSE", "SSE"), #8
    ("S", "S"), #9
    ("SSW", "SSW"), #10
    ("SW", "SW"), #11
    ("WSW", "WSW"), #12
    ("W", "W"), #13
    ("WNW", "WNW"), #14
    ("NW", "NW"), #15
    ("NNW", "NNW"), #16
]
CATEGORY_OF_AUTHORITY = [
    (None, "None"),
    ("customs", "Customs"), #1
    ("border control", "Border Control"), #2
    ("police", "Police"), #3
    ("port", "Port"), #4
    ("immigration", "Immigration"), #5
    ("health", "Health"), #6
    ("coast guard", "Coast Guard"), #7
    ("agricultural", "Agricultural"), #8
    ("military", "Military"), #9
    ("private company", "Private company"), #10
    ("maritime police", "Maritime Police"), #11
    ("environmental", "Environmental"), #12
    ("fishery", "Fishery"), #13
    ("finance", "Finance"), #14
    ("maritime", "Maritime"), #15
]
CATEGORY_OF_CARGO = [
    ("bulk", "bulk"), #1
    ("container", "container"), #2
    ("general", "general"), #3
    ("liquid", "liquid"), #4
    ("passenger", "passenger"), #5
    ("livestock", "livestock"), #6
    ("dangerous or hazardous", "dangerous or hazardous"), #7
]
CATEGORY_OF_COMM_PREF = [
    ("preferred calling", "preferred calling"), #1
    ("alternate calling", "alternate calling"), #2
    ("preferred working", "preferred working"), #3
    ("alternate working", "alternate working"), #4
]
CATEGORY_OF_CONCENTRATION_OF_SHIPPING_HAZARD_AREA = [
    ("concentration of merchant shipping", "concentration of merchant shipping"), #1
    ("concentration of recreational vessels", "concentration of recreational vessels"), #2
    ("concentration of fishing vessels", "concentration of fishing vessels"), #3
    ("concentration of military vessels", "concentration of military vessels"), #4
]
CATEGORY_OF_DANGEROUS_OR_HAZARDOUS_CARGO = [
    ("IMDG Code Class 1 Div. 1.1", "IMDG Code Class 1 Div. 1.1"), #1
    ("IMDG Code Class 1 Div. 1.2", "IMDG Code Class 1 Div. 1.2"), #2
    ("IMDG Code Class 1 Div. 1.3", "IMDG Code Class 1 Div. 1.3"), #3
    ("IMDG Code Class 1 Div. 1.4", "IMDG Code Class 1 Div. 1.4"), #4
    ("IMDG Code Class 1 Div. 1.5", "IMDG Code Class 1 Div. 1.5"), #5
    ("IMDG Code Class 1 Div. 1.6", "IMDG Code Class 1 Div. 1.6"), #6
    ("IMDG Code Class 2 Div. 2.1", "IMDG Code Class 2 Div. 2.1"), #7
    ("IMDG Code Class 2 Div. 2.2", "IMDG Code Class 2 Div. 2.2"), #8
    ("IMDG Code Class 2 Div. 2.3", "IMDG Code Class 2 Div. 2.3"), #9
    ("IMDG Code Class 3", "IMDG Code Class 3"), #10
    ("IMDG Code Class 4 Div. 4.1", "IMDG Code Class 4 Div. 4.1"), #11
    ("IMDG Code Class 4 Div. 4.2", "IMDG Code Class 4 Div. 4.2"), #12
    ("IMDG Code Class 4 Div. 4.3", "IMDG Code Class 4 Div. 4.3"), #13
    ("IMDG Code Class 5 Div. 5.1", "IMDG Code Class 5 Div. 5.1"), #14
    ("IMDG Code Class 5 Div. 5.2", "IMDG Code Class 5 Div. 5.2"), #15
    ("IMDG Code Class 6 Div. 6.1", "IMDG Code Class 6 Div. 6.1"), #16
    ("IMDG Code Class 6. Div. 6.2", "IMDG Code Class 6. Div. 6.2"), #17
    ("IMDG Code Class 7", "IMDG Code Class 7"), #18
    ("IMDG Code Class 8", "IMDG Code Class 8"), #19
    ("IMDG Code Class 9", "IMDG Code Class 9"), #20
    ("Harmful Substances in packaged form", "Harmful Substances in packaged form"), #21
]
CATEGORY_OF_MARITIME_BROADCAST = [
    ("navigational warning", "navigational warning"), #1
    ("meteorological warning", "meteorological warning"), #2
    ("ice report", "ice report"), #3
    ("SAR information", "SAR information"), #4
    ("pirate attack warning", "pirate attack warning"), #5
    ("meteorological forecast", "meteorological forecast"), #6
    ("pilot service message", "pilot service message"), #7
    ("AIS information", "AIS information"), #8
    ("LORAN message", "LORAN message"), #9
    ("SATNAV message", "SATNAV message"), #10
    ("gale warning", "gale warning"), #11
    ("storm warning", "storm warning"), #12
    ("tropical revolving storm warning", "tropical revolving storm warning"), #13
    ("NAVAREA warning", "NAVAREA warning"), #14
    ("coastal warning", "coastal warning"), #15
    ("local warning", "local warning"), #16
    ("low water level warning/negative tidal surge", "low water level warning/negative tidal surge"), #17
    ("icing warning", "icing warning"), #18
    ("tsunami broadcast", "tsunami broadcast"), #19
]
CATEGORY_OF_MILITARY_PRACTICE_AREA = [
    ("torpedo exercise area", "torpedo exercise area"), #2
    ("submarine exercise area", "submarine exercise area"), #3
    ("firing danger area", "firing danger area"), #4
    ("mine-laying practice area", "mine-laying practice area"), #5
    ("small arms firing range", "small arms firing range"), #6
]
CATEGORY_OF_NAVIGATION_LINE = [
    ("Clearing line", "Clearing line"), #1
    ("Transit line", "Transit line"), #2
    ("Leading line bearing a recommended track", "Leading line bearing a recommended track"), #3
]
CATEGORY_OF_PILOT = [
    ("pilot", "pilot"), #1 
    ("deep sea", "deep sea"), #2
    ("harbour", "harbour"), #3
    ("bar", "bar"), #4
    ("river", "river"), #5
    ("channel", "channel"), #6
    ("lake", "lake"), #7
]
CATEGORY_OF_PILOT_BOARDING_PLACE = [
    ("Boarding by pilot-cruising vessel", "Boarding by pilot-cruising vessel"), #1
    ("Boarding by helicopter", "Boarding by helicopter"), #2
    ("Pilot comes out from shore", "Pilot comes out from shore"), #3
]
CATEGORY_OF_RADIO_METHOD = [
    ("Low Frequency (LF) voice traffic", "Low Frequency (LF) voice traffic"), #1
    ("Medium Frequency (MF) voice traffic", "Medium Frequency (MF) voice traffic"), #2
    ("High Frequency (HF) voice traffic", "High Frequency (HF) voice traffic"), #3
    ("Very High Frequency (VHF) voice traffic", "Very High Frequency (VHF) voice traffic"), #4
    ("High Frequency Narrow Band Direct Printing", "High Frequency Narrow Band Direct Printing"), #5
    ("NAVTEX", "NAVTEX"), #6
    ("SafetyNET", "SafetyNET"), #7
    ("NBDP Telegraphy (Narrow Band Direct Printing Telegraphy)", "NBDP Telegraphy (Narrow Band Direct Printing Telegraphy)"), #8
    ("facsimile", "facsimile"), #9
    ("NAVIP", "NAVIP"), #10
    ("Low Frequency (LF) digital traffic", "Low Frequency (LF) digital traffic"), #11
    ("Medium Frequency (MF) digital traffic", "Medium Frequency (MF) digital traffic"), #12
    ("High Frequency (HF) digital traffic", "High Frequency (HF) digital traffic"), #13
    ("Very High Frequency (VHF) digital traffic", "Very High Frequency (VHF) digital traffic"), #14
    ("Low Frequency (LF) telegraph traffic", "Low Frequency (LF) telegraph traffic"), #15
    ("Medium Frequency (MF) telegraph traffic", "Medium Frequency (MF) telegraph traffic"), #16
    ("High Frequency (HF) telegraph traffic", "High Frequency (HF) telegraph traffic"), #17
    ("Medium Frequency (MF) Digital Selective Call traffic", "Medium Frequency (MF) Digital Selective Call traffic"), #18
    ("High Frequency (HF) Digital Selective Call traffic", "High Frequency (HF) Digital Selective Call traffic"), #19
    ("Very High Frequency (VHF) Digital Selective Call traffic", "Very High Frequency (VHF) Digital Selective Call traffic"), #20
]
CATEGORY_OF_RECOMMENDED_TRACK = [
    ("Based on a system of fixed marks", "Based on a system of fixed marks"), #1
    ("Not based on a system of fixed marks", "Not based on a system of fixed marks"), #2
]
CATEGORY_OF_RELATIONSHIP = [
    ("prohibited", "prohibited"), #1
    ("not recommended", "not recommended"), #2
    ("permitted ", "permitted "), # 3
    ("recommended ", "recommended "), # 4
    ("required ", "required "), # 5
    ("not required", "not required"), #6
]
CATEGORY_OF_RESTRICTED_AREA = [
    ("nature reserve", "nature reserve"), #4
    ("bird sanctuary", "bird sanctuary"), #5
    ("game reserve", "game reserve"), #6
    ("seal sanctuary", "seal sanctuary"), #7
    ("historic wreck area", "historic wreck area"), #10
    ("research area", "research area"), #20
    ("fish sanctuary", "fish sanctuary"), #22
    ("ecological reserve", "ecological reserve"), #23
    ("environmentally sensitive sea area", "environmentally sensitive sea area"), #27
    ("particularly sensitive sea area", "particularly sensitive sea area"), #28
    ("coral sanctuary", "coral sanctuary"), #31
    ("recreation area", "recreation area"), #32
]
CATEGORY_OF_ROUTEING_MEASURE = [
    ("archipelagic sea lane", "archipelagic sea lane"), #1
    ("deep water route", "deep water route"), #2
    ("fairway system", "fairway system"), #3
    ("recommended route", "recommended route"), #4
    ("traffic separation scheme", "traffic separation scheme"), #5
    ("two-way route", "two-way route"), #6
]
CATEGORY_OF_RXN = [
    ("navigation", "navigation"), #1
    ("communication", "communication"), #2
    ("environmental protection", "environmental protection"), #3
    ("wildlife protection", "wildlife protection"), #4
    ("security", "security"), #5
    ("customs", "customs"), #6
    ("cargo operation", "cargo operation"), #7
    ("refuge", "refuge"), #8
    ("natural resources or exploitation", "natural resources or exploitation"), #9
    ("port", "port"), #10
    ("finance", "finance"), #11
    ("agriculture", "agriculture"), #12
]
CATEGORY_OF_SCHEDULE = [
    ("normal operation", "normal operation"), #1
    ("closure", "closure"), #2
    ("unmanned operation", "unmanned operation"), #3
]
CATEGORY_OF_SHIP_REPORT = [
    ("sailing plan", "sailing plan"), #1
    ("position report", "position report"), #2
    ("deviation report", "deviation report"), #3
    ("final report", "final report"), #4
    ("dangerous goods report", "dangerous goods report"), #5
    ("harmful substances report", "harmful substances report"), #6
    ("marine pollutants report", "marine pollutants report"), #7
    ("any other report", "any other report"), #8
]
CATEGORY_OF_SIGNAL_STATION_TRAFFIC = [
    ("Port control", "Port control"), #1
    ("Port entry and departure", "Port entry and departure"), #2
    ("International port traffic", "International port traffic"), #3
    ("Berthing", "Berthing"), #4
    ("Dock", "Dock"), #5
    ("Lock", "Lock"), #6
    ("Flood barrage", "Flood barrage"), #7
    ("Bridge passage", "Bridge passage"), #8
    ("Dredging", "Dredging"), #9
    ("Traffic control light", "Traffic control light"), #10
]
CATEGORY_OF_SIGNAL_STATION_WARNING = [
    ("Danger", "Danger"), #1
    ("Maritime obstruction", "Maritime obstruction"), #2
    ("Cable", "Cable"), #3
    ("Military practice", "Military practice"), #4
    ("Distress", "Distress"), #5
    ("Weather", "Weather"), #6
    ("Storm", "Storm"), #7
    ("Ice", "Ice"), #8
    ("Time", "Time"), #9
    ("Tide", "Tide"), #10
    ("Tidal stream", "Tidal stream"), #11
    ("Tide gauge", "Tide gauge"), #12
    ("Tide scale", "Tide scale"), #13
    ("Diving", "Diving"), #14
    ("Water level gauge", "Water level gauge"), #15
]
CATEGORY_OF_TEXT = [
    ("abstract or summary", "abstract or summary"), #1
    ("extract", "extract"), #2
    ("full text", "full text"), #3
]
CATEGORY_OF_TRAFFIC_SEPARATION_SCHEME = [
    ("IMO - adopted", "IMO - adopted"), #1
    ("Not IMO - adopted", "Not IMO - adopted"), #2
]
CATEGORY_OF_VESSEL = [
    ("general cargo vessel", "general cargo vessel"), #1
    ("container carrier", "container carrier"), #2
    ("tanker", "tanker"), #3
    ("bulk carrier", "bulk carrier"), #4
    ("passenger vessel", "passenger vessel"), #5
    ("roll-on roll-off", "roll-on roll-off"), #6
    ("refrigerated cargo vessel", "refrigerated cargo vessel"), #7
    ("fishing vessel", "fishing vessel"), #8
    ("service", "service"), #9
    ("warship", "warship"), #10
    ("towed or pushed composite unit", "towed or pushed composite unit"), #11
    ("tugandtow", "tugandtow"), #12
    ("light recreational", "light recreational"), #13
    ("semi-submersible offshore installation", "semi-submersible offshore installation"), #14
    ("jackup exploration or project installation", "jackup exploration or project installation"), #15
    ("livestock carrier", "livestock carrier"), #16
    ("sport fishing", "sport fishing"), #17
]
CATEGORY_OF_VESSEL_REGISTRY = [
    ("domestic", "domestic"), #1
    ("foreign", "foreign"), #2
]
CATEGORY_OF_VESSEL_TRAFFIC_SERVICE = [
    ("Information Service", "Information Service"), #1
    ("Traffic Organisation Service", "Traffic Organisation Service"), #2
    ("Navigational Assistance Service", "Navigational Assistance Service"), #3
    ("Ship Reporting Service", "Ship Reporting Service"), #4
    ("Local Port Service", "Local Port Service"), #5
]
COMPARISON_OPERATOR = [
    ("greater than", "greater than"), #1
    ("greater than or equal to", "greater than or equal to"), #2
    ("less than", "less than"), #3
    ("less than or equal to", "less than or equal to"), #4
    ("equal to", "equal to"), #5
    ("not equal to", "not equal to"), #6
]
DAY_OF_WEEK = [
    ("monday", "Monday"), #1
    ("tuesday", "Tuesday"), #2
    ("wednesday", "Wednesday"), #3
    ("thursday", "Thursday"), #4
    ("friday", "Friday"), #5
    ("saturday", "Saturday"), #6
    ("sunday", "Sunday"), #7
]
ISPS_LEVEL = [
    ("ISPS Level 1", "ISPS Level 1"), #1
    ("ISPS Level 2", "ISPS Level 2"), #2
    ("ISPS Level 3", "ISPS Level 3"), #3
]
JURISDICTION = [
    ("international", "international"), #1 
    ("national", "national"), #2
    ("national sub-division", "national sub-division"), #3
]
LOGICAL_CONNECTIVES = [
    ("logical conjunction", "logical conjunction"), #1
    ("logical disjunction", "logical disjunction"), #2
]
MEMBERSHIP = [
    ("included", "Included"), #1
    ("excluded", "Excluded"), #2
]
ONLINE_FUNCTION = [
    ("download", "download"), #1
    ("information", "information"), #2
    ("offlineAccess", "offlineAccess"), #3
    ("order", "order"), #4
    ("search", "search"), #5
    ("completeMetadata", "completeMetadata"), #6
    ("browseGraphic", "browseGraphic"), #7
    ("upload", "upload"), #8
    ("em ailService", "em ailService"), #9
    ("browsing", "browsing"), #10
    ("fileAccess", "fileAccess"), #11
]
OPERATION = [
    ("largest value", "largest value"), #1 
    ("smallest value", "smallest value"), #2
]
PILOT_MOVEMENT = [
    ("embarkation", "embarkation"), #1
    ("disembarkation", "disembarkation"), #2
    ("pilot change", "pilot change"), #3
]
PILOT_QUALIFICATION = [
    ("government pilot", "government pilot"), #1
    ("pilot approved by government", "pilot approved by government"), #2
    ("state pilot", "state pilot"), #3
    ("federal pilot", "federal pilot"), #4
    ("company pilot", "company pilot"), #5
    ("local pilot", "local pilot"), #6
    ("citizen with sufficient local knowledge", "citizen with sufficient local knowledge"), #7
    ("citizen with doubtful local knowledge", "citizen with doubtful local knowledge"), #8
]
RESTRICTION = [
    ("anchoring prohibited", "anchoring prohibited"), #1
    ("anchoring restricted", "anchoring restricted"), #2
    ("fishing prohibited", "fishing prohibited"), #3
    ("fishing restricted", "fishing restricted"), #4
    ("trawling prohibited", "trawling prohibited"), #5
    ("trawling restricted", "trawling restricted"), #6
    ("entry prohibited", "entry prohibited"), #7
    ("entry restricted", "entry restricted"), #8
    ("dredging prohibited", "dredging prohibited"), #9
    ("dredging restricted", "dredging restricted"), #10
    ("diving prohibited", "diving prohibited"), #11
    ("diving restricted", "diving restricted"), #12
    ("no wake", "no wake"), #13
    ("area to be avoided", "area to be avoided"), #14
    ("construction prohibited", "construction prohibited"), #15
    ("discharging prohibited", "discharging prohibited"), #16
    ("discharging restricted", "discharging restricted"), #17
    ("industrial or mineral exploration/development prohibited", "industrial or mineral exploration/development prohibited"), #18
    ("industrial or mineral exploration/development restricted", "industrial or mineral exploration/development restricted"), #19
    ("drilling prohibited", "drilling prohibited"), #20
    ("drilling restricted", "drilling restricted"), #21
    ("removal of historical artifacts prohibited", "removal of historical artifacts prohibited"), #22
    ("cargo transhipment (lightering) prohibited", "cargo transhipment (lightering) prohibited"), #23
    ("dragging prohibited", "dragging prohibited"), #24
    ("stopping prohibited", "stopping prohibited"), #25
    ("landing prohibited", "landing prohibited"), #26
    ("speed restricted", "speed restricted"), #27
    ("swimming prohibited", "swimming prohibited"), #28
]
SOURCE_TYPE = [
    ("law or regulation", "law or regulation"), #1
    ("official publication", "official publication"), #2
    ("mariner report, confirmed", "mariner report, confirmed"), #7
    ("mariner report, not confirmed", "mariner report, not confirmed"), #8
    ("industry publications and reports", "industry publications and reports"), #9
    ("remotely sensed images", "remotely sensed images"), #10
    ("photographs", "photographs"), #11
    ("products issued by HO services", "products issued by HO services"), #12
    ("news media", "news media"), #13
    ("traffic data", "traffic data"), #14
]
STATUS = [
    ("permanent", "permanent"), #1
    ("occasional", "occasional"), #2
    ("recommended", "recommended"), #3
    ("not in use", "not in use"), #4
    ("periodic/intermittent", "periodic/intermittent"), #5
    ("reserved", "reserved"), #6
    ("temporary", "temporary"), #7
    ("private", "private"), #8
    ("mandatory", "mandatory"), #9
    ("extinguished", "extinguished"), #11
    ("illuminated", "illuminated"), #12
    ("historic", "historic"), #13
    ("public", "public"), #14
    ("synchronised", "synchronised"), #15
    ("watched", "watched"), #16
    ("un-watched", "un-watched"), #17
    ("existence doubtful", "existence doubtful"), #18
    ("buoyed", "buoyed"), #28
]
TELECOMMUNICATIONS_SERVICE = [
    ("voice", "voice"), #1
    ("facsimile", "facsimile"), #2
    ("sms", "sms"), #3
    ("data", "data"), #4
    ("streamedData", "streamedData"), #5
    ("telex", "telex"), #6
    ("telegraph", "telegraph"), #7
    ("email", "email"), #8
]
TIME_REFERENCE = [
    ("localTime", "Local Time"), #1 
    ("UTC", "UTC"), #2
]
TRAFFIC_FLOW = [
    ("Inbound", "Inbound"), #1
    ("Outbound", "Outbound"), #2
    ("One-way", "One-way"), #3
    ("Two-way", "Two-way"), #4
]
VESSEL_CHARACTERISTICS = [
    ("length overall", "length overall"), #1
    ("length at waterline", "length at waterline"), #2
    ("breadth", "breadth"), #3
    ("draught", "draught"), #4
    ("height", "height"), #5
    ("displacement tonnage", "displacement tonnage"), #6
    ("displacement tonnage, light", "displacement tonnage, light"), #7
    ("displacement tonnage, loaded", "displacement tonnage, loaded"), #8
    ("deadweight tonnage", "deadweight tonnage"), #9
    ("gross tonnage", "gross tonnage"), #10
    ("net tonnage", "net tonnage"), #11
    ("Panama Canal/Universal Measurement System net tonnage", "Panama Canal/Universal Measurement System net tonnage"), #12
    ("Suez Canal net tonnage", "Suez Canal net tonnage"), #13
    ("Suez Canal gross tonnage", "Suez Canal gross tonnage"), #14
]
VESSEL_CHARACTERISTICS_UNIT = [
    ("metre", "metre"), #1
    ("foot", "foot"), #2
    ("metric ton", "metric ton"), #3
    ("ton", "ton"), #4
    ("short ton", "short ton"), #5
    ("gross ton", "gross ton"), #6
    ("net ton", "net ton"), #7
    ("Panama Canal/Universal Measurement System net tonnage", "Panama Canal/Universal Measurement System net tonnage"), #8
    ("Suez Canal Net Tonnage", "Suez Canal Net Tonnage"), #9
    ("none", "none"), #10
    ("cubic metres", "cubic metres"), #11
    ("Suez Canal Gross Tonnage", "Suez Canal Gross Tonnage"), #12
]
