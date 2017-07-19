print "RESTAURANT SEARCH SYSTEM"
Restaurants= {
    "Dominos":
        {
            "Rest_info":
                {
                    "Owner's name":"Rajat",
                    "Rating":4
                },
            "Food_detail":
                {
                    "Small Size Pizza":
                        {
                            "Cost": 200
                        },
                    "Medium Size Pizza":
                        {
                            "Cost": 400
                        },
                    "Large Size Pizza":
                        {
                            "Cost": 600
                        },
                    "Extra Large Size Pizza":
                        {
                            "Cost": 800
                        }
                }
        },
    "Pizza hut":
        {
            "Rest_info":
                {
                    "Owner's name":"Rajat",
                    "Rating":4
                },
            "Food_detail":
                {
                    "Small Size Pizza":
                        {
                            "Cost": 250
                        },
                    "Medium Size Pizza":
                        {
                            "Cost": 450
                        },
                    "Large Size Pizza":
                        {
                            "Cost": 650
                        },
                    "Extra Large Size Pizza":
                        {
                            "Cost": 850
                        }
                }
        }
        }
choice=raw_input("Enter Your choice?\n1.Owner\n2.Customer")
if choice=="1":
    owner_choice=raw_input("You want to update Restaurant's information?:Y/N")
    if owner_choice=="Y":
        ch=raw_input("Enter the name of restaurant:\n1.Dominos\n2.Pizza hut")
        if ch=="1":
            rs=raw_input("what do you want to update")
            if rs=="small":
                Restaurants["Dominos"]["Food_detail"]["Small Size Pizza"]["Cost"]=int(raw_input("Enter the new cost"))
                print Restaurants["Dominos"]["Food_detail"]["Small Size Pizza"]
            elif rs=="medium":
                Restaurants_detail["Dominos"]["Food_detail"]["Medium Size Pizza"]["Cost"]=int(raw_input("Enter the new cost"))
                print Restaurants["Dominos"]["Food_detail"]["Medium Size Pizza"]
            elif rs=="large":
                Restaurants_detail["Dominos"]["Food_detail"]["Small Size Pizza"]["Cost"]=int(raw_input("Enter the new cost"))
                print Restaurants["Dominos"]["Food_detail"]["Large Size Pizza"]
            elif rs=="xl":
                Restaurants_detail["Dominos"]["Food_detail"]["Extra Large Size Pizza"]["Cost"]=int(raw_input("Enter the new cost"))
                print Restaurants["Dominos"]["Food_detail"]["Extra Large Size Pizza"]
        elif ch=="2":
            rs = raw_input("what do you want to update")
            if rs == "small":
                Restaurants["Pizza hut"]["Food_detail"]["Small Size Pizza"]["Cost"] = int(raw_input("Enter the new cost"))
                print Restaurants["Pizza hut"]["Food_detail"]["Small Size Pizza"]
            elif rs == "medium":
                Restaurants["Pizza hut"]["Food_detail"]["Medium Size Pizza"]["Cost"] = int(raw_input("Enter the new cost"))
                print Restaurants["Pizza hut"]["Food_detail"]["Medium Size Pizza"]
            elif rs== "large":
                Restaurants["Pizza hut"]["Food_detail"]["Large Size Pizza"]["Cost"] = int(raw_input("Enter the new cost"))
                print Restaurants["Pizza hut"]["Food_detail"]["Large Size Pizza"]
            elif rs == "xl":
                Restaurants["Pizza hut"]["Food_detail"]["Extra Large Size Pizza"]["Cost"] = int(raw_input("Enter the new cost"))
                print Restaurants["Pizza hut"]["Food_detail"]["Extra Size Pizza"]

    elif owner_choice=="N":
        print "bye bye"

elif choice=="2":
    print Restaurants
    print "order food"
    rest_name=raw_input("Enter the restaurant name from which you want to order the food?\n1.Dominos\n2.Pizza hut")
    if rest_name=="1":
        food_name=raw_input("Enter the food you want to order")
        if food_name in Restaurants["Dominos"]["Food_detail"]:
            print "order successful"
            Restaurants["Dominos"]["Food_detail"][food_name]["Cost"] = Restaurants["Dominos"]["Food_detail"][food_name][
                                                                           "Cost"] + \
                                                                       Restaurants["Dominos"]["Food_detail"][food_name][
                                                                           "Cost"] * 0.15 + \
                                                                       Restaurants["Dominos"]["Food_detail"][food_name][
                                                                           "Cost"] * 0.06
            print "Total cost of the order is", Restaurants["Dominos"]["Food_detail"][food_name]["Cost"]

        else:
                print "order something else"
    elif rest_name=="2":
        food_name = raw_input("Enter the food you want to order")
        if food_name in Restaurants["Pizza hut"]["Food_detail"]:
            print "order successful"
            if rest_name == "1":
                food_name = raw_input("Enter the food you want to order")
                if food_name in Restaurants["Dominos"]["Food_detail"]:
                    print "order successful"
                    Restaurants["Dominos"]["Food_detail"][food_name]["Cost"] = \
                    Restaurants["Dominos"]["Food_detail"][food_name][
                        "Cost"] + \
                    Restaurants["Dominos"]["Food_detail"][food_name][
                        "Cost"] * 0.15 + \
                    Restaurants["Dominos"]["Food_detail"][food_name][
                        "Cost"] * 0.06
                    print "Total cost of the order is", Restaurants["Dominos"]["Food_detail"][food_name]["Cost"]
                    rest_rating = raw_input("Give the Rating to the restaurant?\nYes\nNo")
                    if rest_rating == "Yes":
                        Restaurants["Dominos"]["Rest_info"]["Rating"] = int(raw_input("Enter the rating between 0-5"))
                        print  Restaurants["Pizza hut"]["Rest_info"]["Rating"]
                    elif rest_rating == "No":
                        print "Visit Next Time"
                else:
                    print "order something else"
            elif rest_name == "2":
                food_name = raw_input("Enter the food you want to order")
                if food_name in Restaurants["Pizza hut"]["Food_detail"]:
                    print "order successful"
                    Restaurants["Pizza hut"]["Food_detail"][food_name]["Cost"] = \
                    Restaurants["Pizza hut"]["Food_detail"][food_name]["Cost"] + \
                    Restaurants["Pizza hut"]["Food_detail"][food_name]["Cost"] * 0.15 + \
                    Restaurants["Pizza hut"]["Food_detail"][food_name]["Cost"] * 0.06
                    print "Total cost of the order is", Restaurants["Dominos"]["Food_detail"][food_name]["Cost"]
                    rest_rating = raw_input("Give the Rating to the restaurant?\nYes\nNo")
                    if rest_rating=="Yes":
                        Restaurants["Pizza hut"]["Rest_Info"]["Rating"]=int(raw_input("Enter the rating between 0-5"))
                        print  Restaurants["Pizza hut"]["Rest_info"]["Rating"]
                    elif rest_rating=="No":
                        print "Visit Next Time"
                else:
                    print "order something else"
        else:
                print "order something else"
else:
    print "please enter a valid restaurant name"




















