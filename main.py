import urllib.request
ain = "2861017064"
jfile = open("/Volumes/Kupyn External/Assessor data/jsondata2.txt", "a")
while int(ain) < 8951927520:
    page = urllib.request.urlopen("http://maps.assessor.lacounty.gov/Geocortex/Essentials/REST/sites/PAIS/SQLAINSearch?f=json&AIN=" + str(ain) + "&dojo.preventCache=1435710125197")
    pagetext = page.readlines()
    pagestr = ""
    for hop in pagetext:
        pagestr += str(hop)
    if "FormattedPreviousAIN" not in pagestr:
        for hop in pagetext:
            jfile.write(str(hop))
        ain = str(int(ain)+1)
    else:
        ainloc = pagestr.index("NextAIN") + 10
        ain = pagestr[ainloc:ainloc+10]
print("Done")
jfile.close()
