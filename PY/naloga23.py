def stevilo_besed(niz):
    niz = niz.strip()
    if niz == "":
        return 0
    besede = niz.split()
    return len(besede)

test_niz = "danes je lep dan."
rezultat = stevilo_besed(test_niz)
print(f"Število besed v '{test_niz}' je: {rezultat}")
