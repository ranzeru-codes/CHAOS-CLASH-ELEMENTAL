advantages={

"Flame":"Gale",
"Hydro":"Flame",
"Gale":"Terra",
"Terra":"Storm",
"Storm":"Hydro",
"Light":"Dark",
"Dark":"Light",
"Neutral":"Neutral"

}


def damage(element,enemy):

    if advantages[element]==enemy:

        return 2

    return 1