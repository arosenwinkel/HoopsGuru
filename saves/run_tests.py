import sqlite3

def select_for_all_pos(target):
    query = "select {} from players where ps1='PG';".format(target)
    result = c.execute(query)
    pg_val = result.fetchone()[0]

    query = "select {} from players where ps1='SG';".format(target)
    result = c.execute(query)
    sg_val = result.fetchone()[0]

    query = "select {} from players where ps1='SF';".format(target)
    result = c.execute(query)
    sf_val = result.fetchone()[0]

    query = "select {} from players where ps1='PF';".format(target)
    result = c.execute(query)
    pf_val = result.fetchone()[0]

    query = "select {} from players where ps1='C';".format(target)
    result = c.execute(query)
    c_val = result.fetchone()[0]

    return (pg_val, sg_val, sf_val, pf_val, c_val)

def print_all_pos(vals, val):
    result = "--- {} ---\n".format(val)
    result += "PG: {}\n".format(vals[0])
    result += "SG: {}\n".format(vals[1])
    result += "SF: {}\n".format(vals[2])
    result += "PF: {}\n".format(vals[3])
    result += "C:  {}\n".format(vals[4])
    result += "\n"

    return result

def get_average(skill, pos):
    if pos == "ALL":
        query = "select avg({}) from players;".format(skill)
    else:
        query = "select avg({}) from players where ps1='{}'".format(skill, pos)

    result = c.execute(query)
    val = result.fetchone()[0]
    return val

def get_max(skill, pos):
    if pos == "ALL":
        query = "select max({}) from players;".format(skill)
    else:
        query = "select max({}) from players where ps1='{}'".format(skill, pos)

    result = c.execute(query)
    val = result.fetchone()[0]
    return val

def get_min(skill, pos):
    if pos == "ALL":
        query = "select min({}) from players;".format(skill)
    else:
        query = "select min({}) from players where ps1='{}'".format(skill, pos)

    result = c.execute(query)
    val = result.fetchone()[0]
    return val

def all_stats(pos):
    output = ""
    output += ("{} Size\n".format(pos))
    output += ("Min Grade: {}\n".format(get_min("SZE", pos)))
    output += ("Avg Grade: {}\n".format(get_average("SZE", pos)))
    output += ("Max Grade: {}\n".format(get_max("SZE", pos)))
    output += ("Avg Height: {}\n".format(get_average("hgt", pos)))
    output += ("Avg Wingspan: {}\n".format(get_average("wng", pos)))
    output += ("\n")

    output += ("{} Athleticism\n".format(pos))
    output += ("Min Grade: {}\n".format(get_min("ATH", pos)))
    output += ("Avg Grade: {}\n".format(get_average("ATH", pos)))
    output += ("Max Grade: {}\n".format(get_max("ATH", pos)))
    output += ("Avg Vertical: {}\n".format(get_average("vrt", pos)))
    output += ("Avg Strength: {}\n".format(get_average("str", pos)))
    output += ("Avg Speed: {}\n".format(get_average("spd", pos)))
    output += ("Avg Fitness: {}\n".format(get_average("fit", pos)))
    output += ("\n")

    output += ("{} Shooting\n".format(pos))
    output += ("Min Grade: {}\n".format(get_min("SHT", pos)))
    output += ("Avg Grade: {}\n".format(get_average("SHT", pos)))
    output += ("Max Grade: {}\n".format(get_max("SHT", pos)))
    output += ("Avg Height: {}\n".format(get_average("hgt", pos)))
    output += ("Avg Range: {}\n".format(get_average("rng", pos)))
    output += ("Avg Handling: {}\n".format(get_average("hnd", pos)))
    output += ("Avg Off-Ball: {}\n".format(get_average("obl", pos)))
    output += ("Avg Consistency: {}\n".format(get_average("cns", pos)))
    output += ("\n")

    output += ("{} Attacking/Post Offense\n".format(pos))
    output += ("Min Grade: {}\n".format(get_min("ATT", pos)))
    output += ("Avg Grade: {}\n".format(get_average("ATT", pos)))
    output += ("Max Grade: {}\n".format(get_max("ATT", pos)))
    output += ("Avg Height: {}\n".format(get_average("hgt", pos)))
    output += ("Avg Layup: {}\n".format(get_average("lay", pos)))
    output += ("Avg Footwork: {}\n".format(get_average("ofw", pos)))
    output += ("Avg Touch: {}\n".format(get_average("tou", pos)))
    output += ("Avg Handling: {}\n".format(get_average("hnd", pos)))
    output += ("Avg Off-Hand: {}\n".format(get_average("off", pos)))
    output += ("Avg Vertical: {}\n".format(get_average("vrt", pos)))
    output += ("Avg Quickness: {}\n".format(get_average("qui", pos)))
    output += ("Avg Strength: {}\n".format(get_average("str", pos)))
    output += ("Avg Aggressiveness: {}\n".format(get_average("agg", pos)))
    output += ("\n")

    output += ("{} Playmaking\n".format(pos))
    output += ("Min Grade: {}\n".format(get_min("PMK", pos)))
    output += ("Avg Grade: {}\n".format(get_average("PMK", pos)))
    output += ("Max Grade: {}\n".format(get_max("PMK", pos)))
    output += ("Avg Height: {}\n".format(get_average("hgt", pos)))
    output += ("Avg Passing: {}\n".format(get_average("pas", pos)))
    output += ("Avg Handling: {}\n".format(get_average("hnd", pos)))
    output += ("Avg Decisions: {}\n".format(get_average("dec", pos)))
    output += ("Avg Vision: {}\n".format(get_average("vis", pos)))
    output += ("Avg Creativity: {}\n".format(get_average("crt", pos)))
    output += ("Avg Ego: {}\n".format(get_average("ego", pos)))
    output += ("\n")

    output += ("{} Perimeter Defense/Help Defense\n".format(pos))
    output += ("Min Grade: {}\n".format(get_min("PMD", pos)))
    output += ("Avg Grade: {}\n".format(get_average("PMD", pos)))
    output += ("Max Grade: {}\n".format(get_max("PMD", pos)))
    output += ("Avg Wingspan: {}\n".format(get_average("wng", pos)))
    output += ("Avg Footwork: {}\n".format(get_average("dfw", pos)))
    output += ("Avg Quickness: {}\n".format(get_average("qui", pos)))
    output += ("Avg Vertical: {}\n".format(get_average("vrt", pos)))
    output += ("Avg Strength: {}\n".format(get_average("str", pos)))
    output += ("Avg Fitness: {}\n".format(get_average("fit", pos)))
    output += ("Avg Coordination: {}\n".format(get_average("coo", pos)))
    output += ("Avg Decisions: {}\n".format(get_average("dec", pos)))
    output += ("Avg Reactions: {}\n".format(get_average("rct", pos)))
    output += ("Avg Anticipation: {}\n".format(get_average("ant", pos)))
    output += ("Avg Focus: {}\n".format(get_average("foc", pos)))
    output += ("Avg Motor: {}\n".format(get_average("mtr", pos)))
    output += ("\n")

    output += ("{} Rebounding\n".format(pos))
    output += ("Min Grade: {}\n".format(get_min("REB", pos)))
    output += ("Avg Grade: {}\n".format(get_average("REB", pos)))
    output += ("Max Grade: {}\n".format(get_max("REB", pos)))
    output += ("Avg Wingspan: {}\n".format(get_average("wng", pos)))
    output += ("Avg Boxout: {}\n".format(get_average("box", pos)))
    output += ("Avg Vertical: {}\n".format(get_average("vrt", pos)))
    output += ("Avg Strength: {}\n".format(get_average("str", pos)))
    output += ("Avg Reactions: {}\n".format(get_average("rct", pos)))
    output += ("Avg Anticipation: {}\n".format(get_average("ant", pos)))
    output += ("Avg Aggressiveness: {}\n".format(get_average("agg", pos)))
    output += ("Avg Motor: {}\n".format(get_average("mtr", pos)))
    output += ("\n")

    return output

log = open("log.txt", "w")
log.write("DIAGNOSTIC RESULTS...\n")
log.close()

log = open("log.txt", "a")

conn = sqlite3.connect('test.univ')
c = conn.cursor()

vals = select_for_all_pos("avg(OVR)")
log.write(print_all_pos(vals, "Average OVR"))

vals = select_for_all_pos("count(*)")
log.write(print_all_pos(vals, "Count"))

vals = select_for_all_pos("avg(hgt)")
log.write(print_all_pos(vals, "Average Height"))

vals = select_for_all_pos("avg(REB)")
log.write(print_all_pos(vals, "Average REB"))

vals = select_for_all_pos("avg(rng)")
log.write(print_all_pos(vals, "Average Range"))

log.write(all_stats("PG"))
log.write(all_stats("SG"))
log.write(all_stats("SF"))
log.write(all_stats("PF"))
log.write(all_stats("C"))

conn.close()
log.close()
