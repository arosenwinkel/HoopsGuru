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

conn.close()
log.close()
