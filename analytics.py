def analytics(registry):
    routes = registry.routes.values()
    if not routes:
        print("registry is empty - analytics unavailable")
    all_routes = sorted([r.name for r in routes])
    above_70 = [r.name for r in routes if r.get_percentage()>70]
    below_70 = [r.name for r in routes if r.get_percentage()<70]
    percentages = [r.get_percentage() for r in routes]
    averages = round(sum(percentages)/len(percentages),1)

    best = max(routes, key = lambda r:r.get_percentage())
    worst = min(routes, key = lambda r:r.get_percentage())

    print(f"""\n 
 ----------------------- Analytics ------------------------------
 All Routes: {all_routes}
 Above 70% : {above_70}
 Below 70% : {below_70}
 Averages : {averages}%
 Best : {best}
 Worst : {worst}
          """)