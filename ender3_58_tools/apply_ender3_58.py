#!/usr/bin/env python3
"""
apply_ender3_58.py
Uebertraegt die eigenen Anpassungen des Ender-3_58 (aus Marlin 2.0.9.2)
auf die Marlin-Beispielconfig "Creality/Ender-3/BigTreeTech SKR Mini E3 1.2".

Aufruf:  python3 apply_ender3_58.py <Marlin-Ordner> <Bericht.txt>
Beispiel: python3 ender3_58_tools/apply_ender3_58.py Marlin ~/Documents/PlatformIO/Ender3_58_Ergebnisse/bericht.txt

- Aendert nur die erste passende #define-Zeile je Option.
- Jede geaenderte Zeile bekommt den Kommentar "// VB Ender-3_58".
- Mehrfaches Ausfuehren ist unschaedlich.
"""
import re
import sys
import pathlib

MARKER = "// VB Ender-3_58"
C = "Configuration.h"
A = "Configuration_adv.h"

# (Datei, Name oder (Name, Alternativname), Aktion, Wert, optional)
#   Aktion: "set" = aktivieren + Wert setzen, "on" = aktivieren, "off" = deaktivieren
CHANGES = [
    # --- Configuration.h: Allgemein ---
    (C, "STRING_CONFIG_H_AUTHOR", "set", '"(VolkmarB, Ender-3_58)"', False),
    (C, "SHOW_BOOTSCREEN", "off", None, False),
    (C, "SHOW_CUSTOM_BOOTSCREEN", "off", None, False),
    (C, "CUSTOM_STATUS_SCREEN_IMAGE", "off", None, False),
    (C, "CUSTOM_MACHINE_NAME", "set", '"Ender-3_58"', False),
    (C, "SERIAL_PORT", "set", "2", False),
    (C, "SERIAL_PORT_2", "set", "-1", False),
    (C, "BAUDRATE", "set", "115200", False),
    # --- Temperatur ---
    (C, "BED_MAXTEMP", "set", "90", False),
    (C, ("DEFAULT_KP", "DEFAULT_Kp"), "set", "51.51", False),
    (C, ("DEFAULT_KI", "DEFAULT_Ki"), "set", "8.68", False),
    (C, ("DEFAULT_KD", "DEFAULT_Kd"), "set", "76.41", False),
    (C, "PIDTEMPBED", "on", None, False),
    (C, ("DEFAULT_BED_KP", "DEFAULT_bedKp"), "set", "70.41", False),
    (C, ("DEFAULT_BED_KI", "DEFAULT_bedKi"), "set", "13.72", False),
    (C, ("DEFAULT_BED_KD", "DEFAULT_bedKd"), "set", "240.81", False),
    (C, "EXTRUDE_MINTEMP", "set", "210", False),
    (C, "PREVENT_LENGTHY_EXTRUDE", "on", None, False),
    (C, "EXTRUDE_MAXLENGTH", "set", "100", False),
    # --- Mechanik ---
    (C, "ENDSTOP_INTERRUPTS_FEATURE", "on", None, False),
    (C, "DEFAULT_AXIS_STEPS_PER_UNIT", "set", "{ 80, 80, 402, 131 }", False),
    (C, "DEFAULT_MAX_FEEDRATE", "set", "{ 500, 500, 10, 60 }", False),
    (C, "LIMITED_MAX_FR_EDITING", "on", None, False),
    (C, "MAX_FEEDRATE_EDIT_VALUES", "set", "{ 600, 600, 20, 80 }", False),
    (C, "DEFAULT_MAX_ACCELERATION", "set", "{ 500, 500, 20, 5000 }", False),
    (C, "DEFAULT_ACCELERATION", "set", "500", False),
    (C, "DEFAULT_RETRACT_ACCELERATION", "set", "500", False),
    (C, "DEFAULT_TRAVEL_ACCELERATION", "set", "500", False),
    (C, "CLASSIC_JERK", "on", None, False),
    (C, "DEFAULT_XJERK", "set", "10.0", False),
    (C, "DEFAULT_YJERK", "set", "10.0", False),
    (C, "DEFAULT_ZJERK", "set", "0.3", False),
    (C, "TRAVEL_EXTRA_XYJERK", "set", "5.0", False),
    (C, "DEFAULT_EJERK", "set", "10.0", False),
    (C, "S_CURVE_ACCELERATION", "on", None, False),
    (C, "INVERT_X_DIR", "set", "true", False),
    (C, "INVERT_Y_DIR", "set", "true", False),
    (C, "INVERT_Z_DIR", "set", "false", False),
    (C, "INVERT_E0_DIR", "set", "true", False),
    # --- Probe ---
    (C, "BLTOUCH", "on", None, False),
    (C, "NOZZLE_TO_PROBE_OFFSET", "set", "{ -45, -8, -2.69 }", False),
    (C, "Z_AFTER_PROBING", "set", "30", False),
    (C, "Z_MIN_PROBE_REPEATABILITY_TEST", "on", None, False),
    (C, "PROBING_FANS_OFF", "on", None, False),
    # --- Homing / Bauraum ---
    (C, "Z_HOMING_HEIGHT", "set", "4", False),
    (C, "Z_AFTER_HOMING", "set", "10", False),
    (C, "X_BED_SIZE", "set", "220", False),
    (C, "Y_BED_SIZE", "set", "220", False),
    (C, "X_MIN_POS", "set", "-10", False),
    (C, "Y_MIN_POS", "set", "-20", False),
    (C, "Z_MAX_POS", "set", "165", False),
    (C, "SOFT_ENDSTOPS_MENU_ITEM", "on", None, False),
    (C, "Z_SAFE_HOMING", "on", None, False),
    (C, "HOMING_FEEDRATE_MM_M", "set", "{ (20*60), (20*60), (8*60) }", False),
    # --- Leveling ---
    (C, "AUTO_BED_LEVELING_BILINEAR", "on", None, False),
    (C, "MESH_BED_LEVELING", "off", None, False),
    (C, "PREHEAT_BEFORE_LEVELING", "on", None, False),
    (C, "LEVELING_NOZZLE_TEMP", "set", "200", False),
    (C, "LEVELING_BED_TEMP", "off", None, False),
    (C, "GRID_MAX_POINTS_X", "set", "3", False),
    (C, ("BED_TRAMMING_INCLUDE_CENTER", "LEVEL_CENTER_TOO"), "on", None, False),
    # --- Preheat ---
    (C, "PREHEAT_1_TEMP_HOTEND", "set", "210", False),
    (C, "PREHEAT_1_TEMP_BED", "set", "60", False),
    (C, "PREHEAT_1_FAN_SPEED", "set", "64", False),
    (C, "PREHEAT_2_LABEL", "set", '"PETG"', False),
    (C, "PREHEAT_2_TEMP_HOTEND", "set", "240", False),
    (C, "PREHEAT_2_TEMP_BED", "set", "70", False),
    (C, "PREHEAT_2_FAN_SPEED", "set", "64", False),
    (C, "NOZZLE_CLEAN_MIN_TEMP", "set", "210", False),
    # --- Luefter ---
    (C, "FAN_SOFT_PWM", "on", None, False),
    (C, "SOFT_PWM_SCALE", "set", "1", False),
    (C, "SOFT_PWM_DITHER", "on", None, False),

    # --- Configuration_adv.h: Thermal ---
    (A, "THERMAL_PROTECTION_PERIOD", "set", "60", False),
    (A, "THERMAL_PROTECTION_HYSTERESIS", "set", "8", False),
    (A, "WATCH_TEMP_PERIOD", "set", "40", False),
    (A, "AUTOTEMP", "on", None, False),
    # --- BLTouch ---
    (A, "BLTOUCH_DELAY", "set", "500", False),
    (A, "BLTOUCH_FORCE_SW_MODE", "on", None, False),
    (A, "BLTOUCH_SET_5V_MODE", "off", None, False),
    # --- Bewegung ---
    (A, "SLOWDOWN_DIVISOR", "set", "8", False),
    # --- LCD ---
    (A, "BEEP_ON_FEEDRATE_CHANGE", "on", None, False),
    (A, "PROBE_OFFSET_WIZARD", "on", None, False),
    (A, "PROBE_OFFSET_WIZARD_START_Z", "set", "-4.0", False),
    (A, "PROBE_OFFSET_WIZARD_XY_POS", "set", "{ X_CENTER, Y_CENTER }", False),
    (A, "TURBO_BACK_MENU_ITEM", "on", None, False),
    (A, "STATUS_CHAMBER_ANIM", "off", None, False),
    (A, ("SET_PROGRESS_MANUALLY", "LCD_SET_PROGRESS_MANUALLY"), "on", None, False),
    (A, "SET_PROGRESS_PERCENT", "on", None, True),
    # --- Babystepping ---
    (A, "BABYSTEP_MULTIPLICATOR_Z", "set", "8", False),
    (A, "BABYSTEP_MULTIPLICATOR_XY", "set", "10", False),
    (A, "BABYSTEP_ZPROBE_OFFSET", "on", None, False),
    (A, "BABYSTEP_ZPROBE_GFX_OVERLAY", "on", None, False),
    # --- Probing-Raender ---
    (A, "PROBING_MARGIN_LEFT", "set", "10", False),
    (A, "PROBING_MARGIN_RIGHT", "set", "10", False),
    (A, "PROBING_MARGIN_FRONT", "set", "10", False),
    (A, "PROBING_MARGIN_BACK", "set", "10", False),
    # --- Linear Advance (wie bisher, K=0) ---
    (A, "LIN_ADVANCE", "on", None, False),
    # ADVANCE_K bleibt Standard 0.0 (nicht anfassen, Wert existiert 2x)
    (A, "EXPERIMENTAL_SCURVE", "on", None, True),
    # --- Puffer ---
    (A, "BUFSIZE", "set", "32", False),
    (A, "TX_BUFFER_SIZE", "set", "32", False),
    (A, "EMERGENCY_PARSER", "on", None, False),
    # --- M600 Filamentwechsel ---
    (A, "ADVANCED_PAUSE_FEATURE", "on", None, False),
    (A, "FILAMENT_CHANGE_UNLOAD_LENGTH", "set", "100", False),
    (A, "FILAMENT_CHANGE_FAST_LOAD_LENGTH", "set", "100", False),
    (A, "ADVANCED_PAUSE_PURGE_LENGTH", "set", "40", False),
    (A, "ADVANCED_PAUSE_FANS_PAUSE", "on", None, False),
    (A, "FILAMENT_CHANGE_ALERT_BEEPS", "set", "3", False),
    (A, "PARK_HEAD_ON_PAUSE", "on", None, False),
    (A, "HOME_BEFORE_FILAMENT_CHANGE", "on", None, False),
    # --- Motorstroeme ---
    (A, "X_CURRENT", "set", "590", False),
    (A, "Y_CURRENT", "set", "590", False),
    (A, "Z_CURRENT", "set", "1180", False),
    (A, "E0_CURRENT", "set", "700", False),
    # --- Host ---
    (A, "HOST_ACTION_COMMANDS", "on", None, False),
    (A, "HOST_PAUSE_M76", "on", None, False),
    (A, "HOST_PROMPT_SUPPORT", "on", None, False),
    # --- Verbesserungen 2.1.2.9 ---
    (C, "RESTORE_LEVELING_AFTER_G28", "on", None, False),  # M1
    (A, "STEALTHCHOP_E", "off", None, False),  # M3 (Linear Advance)
    (A, "INPUT_SHAPING_X", "on", None, False),  # M4
    (A, "INPUT_SHAPING_Y", "on", None, False),  # M4
    (A, "SHAPING_MIN_FREQ", "set", "20.0", False),  # M4
    (A, "SHAPING_MENU", "on", None, False),  # M4
]

# Nur pruefen und berichten (nicht aendern)
CHECKS = {
    C: ["CONFIGURATION_H_VERSION", "MOTHERBOARD", "X_DRIVER_TYPE", "E0_DRIVER_TYPE",
        "CR10_STOCKDISPLAY", "SDSUPPORT", "EEPROM_SETTINGS", "EEPROM_AUTO_INIT",
        "FILAMENT_RUNOUT_SENSOR", "NOZZLE_PARK_FEATURE", "LCD_BED_LEVELING",
        "MESH_EDIT_MENU", "LCD_BED_TRAMMING", "LEVEL_BED_CORNERS",
        "RESTORE_LEVELING_AFTER_G28", "ENABLE_LEVELING_AFTER_G28",
        "EXTRAPOLATE_BEYOND_GRID", "DEFAULT_LEVELING_FADE_HEIGHT", "PROBING_MARGIN",
        "Z_PROBE_FEEDRATE_FAST", "MULTIPLE_PROBING", "PRINTCOUNTER",
        "INDIVIDUAL_AXIS_HOMING_MENU", "LCD_LANGUAGE", "SPEAKER", "BED_TRAMMING_INSET_LFRB",
        "LEVEL_CORNERS_INSET_LFRB"],
    A: ["CONFIGURATION_ADV_H_VERSION", "QUICK_HOME", "NUM_Z_STEPPER_DRIVERS",
        "BLTOUCH_HS_MODE", "ARC_SUPPORT", "INPUT_SHAPING_X", "INPUT_SHAPING_Y",
        "MEATPACK_ON_SERIAL_PORT_1", "MEATPACK_ON_SERIAL_PORT_2",
        "POWER_LOSS_RECOVERY", "SDCARD_SORT_ALPHA", "SDSORT_USES_RAM",
        "SDSORT_CACHE_NAMES", "LONG_FILENAME_HOST_SUPPORT", "SCROLL_LONG_FILENAMES",
        "EVENT_GCODE_SD_ABORT", "SD_FINISHED_RELEASECOMMAND", "AUTO_REPORT_TEMPERATURES",
        "EXTENDED_CAPABILITIES_REPORT", "FILAMENT_LOAD_UNLOAD_GCODES",
        "STEALTHCHOP_XY", "STEALTHCHOP_Z", "STEALTHCHOP_E", "HYBRID_THRESHOLD",
        "SQUARE_WAVE_STEPPING", "CHOPPER_TIMING", "LCD_INFO_MENU", "BLOCK_BUFFER_SIZE",
        "SERIAL_OVERRUN_PROTECTION", "SHOW_REMAINING_TIME", "SET_REMAINING_TIME",
        "M73_REPORT", "DOUBLECLICK_FOR_Z_BABYSTEPPING", "SERIAL_FLOAT_PRECISION",
        "FASTER_GCODE_PARSER", "USE_WATCHDOG"],
}


def define_regex(name):
    return re.compile(
        r'^(?P<ind>[ \t]*)(?P<cm>//[ \t]*)?#define[ \t]+' + re.escape(name)
        + r'(?=[ \t]|$)(?P<rest>.*)$', re.M)


def split_comment(rest):
    """Trennt Wert und Kommentar (// ausserhalb von Anfuehrungszeichen)."""
    q = False
    for i, ch in enumerate(rest):
        if ch == '"':
            q = not q
        elif not q and rest.startswith("//", i):
            return rest[:i], rest[i:]
    return rest, ""


def strip_marker(s):
    return s.replace("  " + MARKER, "").replace(" " + MARKER, "").replace(MARKER, "").rstrip()


def apply(text, names, action, value):
    for name in names:
        m = define_regex(name).search(text)
        if not m:
            continue
        old = m.group(0)
        ind, cm = m.group("ind"), m.group("cm")
        rest = strip_marker(m.group("rest"))
        valpart, comment = split_comment(rest)
        if action == "off":
            if cm:
                return text, name, "bereits aus", old, old
            new = ind + "//#define " + name + rest
        elif action == "on":
            new = ind + "#define " + name + rest
        else:  # set
            lead = re.match(r'[ \t]*', valpart).group(0) or " "
            body = valpart[len(lead):]
            new = ind + "#define " + name + lead + value
            if comment:
                pad = max(1, len(body) - len(value)) if body.strip() else 1
                new += " " * pad + comment.rstrip()
        if action != "off":
            new = new.rstrip() + "  " + MARKER
        new = new.rstrip()
        status = "unveraendert" if strip_marker(new) == strip_marker(old) and (cm is None) == (action != "off") else "geaendert"
        text = text[:m.start()] + new + text[m.end():]
        return text, name, status, old, new
    return text, names[0], "NICHT GEFUNDEN", "", ""


def state_line(text, name):
    m = define_regex(name).search(text)
    if not m:
        return "nicht vorhanden"
    val, _ = split_comment(strip_marker(m.group("rest")))
    return ("AUS " if m.group("cm") else "AN  ") + val.strip()


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    mdir = pathlib.Path(sys.argv[1])
    report = pathlib.Path(sys.argv[2]).expanduser()
    files = {f: (mdir / f).read_text(encoding="utf-8") for f in (C, A)}
    lines, errors = [], 0

    lines.append("=== Uebertragene Einstellungen ===")
    for f, names, action, value, optional in CHANGES:
        names = names if isinstance(names, tuple) else (names,)
        files[f], used, status, old, new = apply(files[f], names, action, value)
        if status == "NICHT GEFUNDEN":
            status = "optional, nicht vorhanden" if optional else status
            if not optional:
                errors += 1
        lines.append(f"[{status:>25}] {f:<20} {used}")
        if status == "geaendert":
            lines.append(f"      alt: {old.strip()}")
            lines.append(f"      neu: {new.strip()}")

    for f in (C, A):
        (mdir / f).write_text(files[f], encoding="utf-8")

    lines.append("")
    lines.append("=== Kontrolle (nicht geaendert) ===")
    for f, names in CHECKS.items():
        for n in names:
            lines.append(f"{f:<20} {n:<32} {state_line(files[f], n)}")

    lines.append("")
    lines.append(f"Fehler (nicht gefunden): {errors}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Fertig. Fehler: {errors}. Bericht: {report}")


if __name__ == "__main__":
    main()
