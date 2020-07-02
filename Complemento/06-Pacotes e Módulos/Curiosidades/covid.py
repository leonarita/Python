from covid import Covid

covid = Covid()


def covid_worldwide():
    print(covid.get_total_active_cases())
    print(covid.get_total_confirmed_cases())
    print(covid.get_total_recovered())
    print(covid.get_total_deaths())


covid_worldwide()