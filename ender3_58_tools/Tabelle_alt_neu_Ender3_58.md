# Ender-3_58 – Übertragene Einstellungen alt → neu

Stand: 26.10.2026 · Alt: Marlin 2.0.9.2 (laufende Firmware) · Neu: Marlin 2.1.2.9, Basis Beispielconfig „Creality/Ender-3/BigTreeTech SKR Mini E3 1.2“ (Configurations release-2.1.2.9)
Repo: github.com/azetat/Marlin, Branch `ender3_58` · Werkzeug: `ender3_58_tools/apply_ender3_58.py` · Markierung im Code: `// VB Ender-3_58`

## Configuration.h

| Bereich | Option (2.0.9.2) | Option (2.1.2.9) | Vorlage 2.1.2.9 | Ender-3_58 (alt = neu) |
|---|---|---|---|---|
| Info | STRING_CONFIG_H_AUTHOR | gleich | "(thisiskeithb, Ender-3)" | "(VolkmarB, Ender-3_58)" |
| Info | SHOW_BOOTSCREEN | gleich | an | aus |
| Info | SHOW_CUSTOM_BOOTSCREEN / CUSTOM_STATUS_SCREEN_IMAGE | gleich | an | aus |
| Info | CUSTOM_MACHINE_NAME | gleich | "Ender-3" | "Ender-3_58" |
| Serial | SERIAL_PORT / SERIAL_PORT_2 / BAUDRATE | gleich | 2 / -1 / 115200 | 2 / -1 / 115200 (unverändert) |
| Temperatur | BED_MAXTEMP | gleich | 125 | 90 |
| Temperatur | DEFAULT_Kp / Ki / Kd | **DEFAULT_KP / KI / KD** | 21.73 / 1.54 / 76.55 | 51.51 / 8.68 / 76.41 |
| Temperatur | PIDTEMPBED | gleich | aus | an |
| Temperatur | DEFAULT_bedKp / Ki / Kd | **DEFAULT_BED_KP / KI / KD** | (Vorlage) | 70.41 / 13.72 / 240.81 |
| Extruder | EXTRUDE_MINTEMP | gleich | 170 | 210 |
| Extruder | EXTRUDE_MAXLENGTH | gleich | 600 | 100 |
| Endstops | ENDSTOP_INTERRUPTS_FEATURE | gleich | aus | an |
| Mechanik | DEFAULT_AXIS_STEPS_PER_UNIT | gleich | { 80, 80, 400, 93 } | { 80, 80, 402, 131 } |
| Mechanik | DEFAULT_MAX_FEEDRATE | gleich | { 500, 500, 5, 25 } | { 500, 500, 10, 60 } |
| Mechanik | LIMITED_MAX_FR_EDITING | gleich | aus | an |
| Mechanik | MAX_FEEDRATE_EDIT_VALUES | gleich | { 600, 600, 10, 50 } | { 600, 600, 20, 80 } |
| Mechanik | DEFAULT_MAX_ACCELERATION | gleich | { 500, 500, 100, 5000 } | { 500, 500, 20, 5000 } |
| Mechanik | DEFAULT_ACCELERATION / RETRACT / TRAVEL | gleich | 500 / 500 / 500 | 500 / 500 / 500 (unverändert) |
| Mechanik | CLASSIC_JERK | gleich | aus | an |
| Mechanik | DEFAULT_X/Y/ZJERK | gleich | 10 / 10 / 0.3 | 10 / 10 / 0.3 (unverändert) |
| Mechanik | TRAVEL_EXTRA_XYJERK | gleich | aus (0.0) | 5.0 |
| Mechanik | DEFAULT_EJERK | gleich | 5.0 | 10.0 |
| Mechanik | S_CURVE_ACCELERATION | gleich | an | an (unverändert) |
| Mechanik | INVERT_X/Y/Z/E0_DIR | gleich | true / true / false / true | unverändert |
| Probe | BLTOUCH | gleich | aus | an |
| Probe | NOZZLE_TO_PROBE_OFFSET | gleich | { 10, 10, 0 } | **{ -45, -8, -2.69 }** (Z bisher nur im EEPROM) |
| Probe | Z_AFTER_PROBING | gleich | aus (5) | 30 |
| Probe | Z_MIN_PROBE_REPEATABILITY_TEST (M48) | gleich | aus | an |
| Probe | PROBING_FANS_OFF | gleich | aus | an |
| Homing | Z_HOMING_HEIGHT / Z_AFTER_HOMING | gleich | aus | 4 / 10 |
| Homing | Z_SAFE_HOMING | gleich | aus | an |
| Homing | HOMING_FEEDRATE_MM_M | gleich | Z 4*60 | Z 8*60 |
| Bauraum | X_BED_SIZE / Y_BED_SIZE | gleich | 235 / 235 | 220 / 220 |
| Bauraum | X_MIN_POS / Y_MIN_POS | gleich | 0 / 0 | -10 / -20 |
| Bauraum | Z_MAX_POS | gleich | 250 | 165 (bewusst, Micro Swiss) |
| Bauraum | SOFT_ENDSTOPS_MENU_ITEM | gleich | aus | an |
| Leveling | AUTO_BED_LEVELING_BILINEAR / MESH_BED_LEVELING | gleich | MBL | ABL Bilinear |
| Leveling | PREHEAT_BEFORE_LEVELING | gleich | aus | an |
| Leveling | LEVELING_NOZZLE_TEMP / LEVELING_BED_TEMP | gleich | 120 / 50 | 200 / aus |
| Leveling | GRID_MAX_POINTS_X | gleich | 5 | 3 |
| Leveling | LEVEL_BED_CORNERS | **LCD_BED_TRAMMING** | an | an (unverändert) |
| Leveling | LEVEL_CORNERS_INSET_LFRB | **BED_TRAMMING_INSET_LFRB** | { 30, 30, 30, 30 } | unverändert |
| Leveling | LEVEL_CENTER_TOO | **BED_TRAMMING_INCLUDE_CENTER** | aus | an |
| Preheat | PREHEAT_1 (PLA) Hotend / Bett / Lüfter | gleich | 185 / 45 / 255 | 210 / 60 / 64 |
| Preheat | PREHEAT_2 Label / Hotend / Bett / Lüfter | gleich | "ABS" 240 / 110 / 255 | "PETG" 240 / 70 / 64 |
| Preheat | NOZZLE_CLEAN_MIN_TEMP | gleich | 170 | 210 |
| Lüfter | FAN_SOFT_PWM / SOFT_PWM_SCALE / SOFT_PWM_DITHER | gleich | aus / 0 / aus | an / 1 / an |

## Configuration_adv.h

| Bereich | Option (2.0.9.2) | Option (2.1.2.9) | Vorlage 2.1.2.9 | Ender-3_58 (alt = neu) |
|---|---|---|---|---|
| Thermal | THERMAL_PROTECTION_PERIOD / HYSTERESIS | gleich | 40 / 4 | 60 / 8 |
| Thermal | WATCH_TEMP_PERIOD | gleich | 40 | 40 (unverändert) |
| Thermal | AUTOTEMP | gleich | an | an (unverändert) |
| BLTouch | BLTOUCH_DELAY | gleich | aus | 500 |
| BLTouch | BLTOUCH_FORCE_SW_MODE | gleich | aus | an |
| BLTouch | BLTOUCH_SET_5V_MODE | gleich | aus | aus (OD-Modus, bleibt) |
| Bewegung | SLOWDOWN_DIVISOR | gleich | 2 | 8 |
| LCD | BEEP_ON_FEEDRATE_CHANGE | gleich | aus | an |
| LCD | PROBE_OFFSET_WIZARD (+ START_Z -4.0, XY_POS Mitte) | gleich | aus | an |
| LCD | TURBO_BACK_MENU_ITEM | gleich | aus | an |
| LCD | STATUS_CHAMBER_ANIM | gleich | an | aus |
| LCD | LCD_SET_PROGRESS_MANUALLY (M73) | **SET_PROGRESS_MANUALLY + SET_PROGRESS_PERCENT** | an | an (unverändert) |
| Babystep | BABYSTEP_MULTIPLICATOR_Z / XY | gleich | 1 / 1 | 8 / 10 |
| Babystep | BABYSTEP_ZPROBE_OFFSET + GFX_OVERLAY | gleich | aus | an |
| Probing | PROBING_MARGIN_LEFT/RIGHT/FRONT/BACK | gleich | aus (= PROBING_MARGIN) | 10 / 10 / 10 / 10 |
| Lin. Advance | LIN_ADVANCE | gleich | an | an (unverändert) |
| Lin. Advance | LIN_ADVANCE_K | **ADVANCE_K** | 0.0 | 0.0 (unverändert, nicht kalibriert) |
| Lin. Advance | EXPERIMENTAL_SCURVE | **entfallen** | – | – (in 2.1.2.x nicht mehr nötig) |
| Puffer | BUFSIZE / TX_BUFFER_SIZE | gleich | 4 / 0 | 32 / 32 |
| Puffer | EMERGENCY_PARSER | gleich | an | an (unverändert) |
| M600 | ADVANCED_PAUSE_FEATURE | gleich | an | an (unverändert) |
| M600 | FILAMENT_CHANGE_UNLOAD_LENGTH / FAST_LOAD_LENGTH | gleich | 400 / 350 | 100 / 100 |
| M600 | ADVANCED_PAUSE_PURGE_LENGTH | gleich | 50 | 40 |
| M600 | ADVANCED_PAUSE_FANS_PAUSE | gleich | aus | an |
| M600 | FILAMENT_CHANGE_ALERT_BEEPS | gleich | 10 | 3 |
| M600 | PARK_HEAD_ON_PAUSE / HOME_BEFORE_FILAMENT_CHANGE | gleich | aus | an |
| TMC | X / Y / Z / E0_CURRENT (mA) | gleich | 580 / 580 / 580 / 650 | 590 / 590 / **1180** / 700 |
| Host | HOST_ACTION_COMMANDS / HOST_PAUSE_M76 / HOST_PROMPT_SUPPORT | gleich | aus | an |

## Umbenannt / entfallen (Überblick)

| 2.0.9.2 | 2.1.2.9 |
|---|---|
| DEFAULT_Kp/Ki/Kd | DEFAULT_KP/KI/KD |
| DEFAULT_bedKp/Ki/Kd | DEFAULT_BED_KP/KI/KD |
| LEVEL_BED_CORNERS | LCD_BED_TRAMMING |
| LEVEL_CORNERS_INSET_LFRB | BED_TRAMMING_INSET_LFRB |
| LEVEL_CENTER_TOO | BED_TRAMMING_INCLUDE_CENTER |
| LCD_SET_PROGRESS_MANUALLY | SET_PROGRESS_MANUALLY (+ SET_PROGRESS_PERCENT) |
| LIN_ADVANCE_K | ADVANCE_K |
| EXPERIMENTAL_SCURVE | entfallen |
| NUM_Z_STEPPER_DRIVERS | entfallen (Z2_DRIVER_TYPE); Dual-Z an einem Treiber braucht nichts |

## Abweichungen der neuen Vorlage, bewusst noch nicht übernommen (→ Teil d)

| Option | 2.0.9.2 | 2.1.2.9 Vorlage |
|---|---|---|
| BLOCK_BUFFER_SIZE | 16 | 16 wirksam (8 nur bei DIRECT_STEPPING) – keine Änderung nötig |
| BLTOUCH_HS_MODE | aus | aus |
| ARC_SUPPORT, INPUT_SHAPING, MEATPACK | aus | aus |

## Verbesserungen nach Migration (2.1.2.9)

| Nr | Option | Datei | Vorlage | Ender-3_58 | Grund |
|---|---|---|---|---|---|
| M1 | RESTORE_LEVELING_AFTER_G28 | Configuration.h | aus | an | Mesh bleibt nach G28 aktiv |
| M2 | BLOCK_BUFFER_SIZE | Configuration_adv.h | 16 | 16 | entfällt, bereits 16 |
| M3 | STEALTHCHOP_E | Configuration_adv.h | an | aus | Voraussetzung Linear Advance |
| M4 | INPUT_SHAPING_X / _Y | Configuration_adv.h | aus | an (40 Hz, Zeta 0.15 – noch kalibrieren) | weniger Ringing |
| M4 | SHAPING_MIN_FREQ | Configuration_adv.h | aus (= 40) | 20.0 | Kalibrierung per M593 auch < 40 Hz |
| M4 | SHAPING_MENU | Configuration_adv.h | aus | an | Werte am Display einstellbar |
| B | SET_REMAINING_TIME | Configuration_adv.h | aus | an | Restzeit per M73 R (Plugin M73 Progress) |
| B | SHOW_REMAINING_TIME | Configuration_adv.h | aus | an | Display zeigt Restzeit |
| B | SHOW_ELAPSED_TIME | Configuration_adv.h | an | aus | keine Laufzeit mehr |
| B | SHOW_PROGRESS_PERCENT | Configuration_adv.h | an | aus | kein Wechsel im Zeitfeld, Balken bleibt |
