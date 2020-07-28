#!/usr/local/bin/checkio --domain=py run every-person-is-unique


class Person:
    def __init__(
        self,
        first_name,
        last_name,
        birth_date,
        job,
        working_years,
        salary,
        country,
        city,
        gender="unknown",
    ):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__job = job
        self.__working_years = working_years
        self.__salary = salary
        self.__country = country
        self.__city = city
        self.__gender = gender

    def name(self):
        result = "{} {}".format(self.__first_name, self.__last_name)
        return result

    def age(self):
        result = 2018 - int(self.__birth_date[-4:]) - 1
        return result

    def work(self):
        if self.__gender == "male":
            result = "He is a " + self.__job
        elif self.__gender == "female":
            result = "She is a " + self.__job
        else:
            result = "Is a " + self.__job
        return result

    def money(self):
        result = "{:,}".format(int(self.__working_years * self.__salary * 12))
        result = result.replace(",", " ")
        return result

    def home(self):
        result = "Lives in {}, {}".format(self.__city, self.__country)
        return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person(
        "John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male"
    )
    p2 = Person(
        "Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna"
    )
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
