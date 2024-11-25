from tests_class import TestCase


class TestID:

    def test_first(self):
        test_case = TestCase()
        id_new_animal = test_case.create_animal('Orlock')
        id_find_animal = test_case.find_animal(id_new_animal)['id']

        assert id_new_animal == id_find_animal, (
            "[FAILED]: Ids doesnt match {} and {}".format(id_new_animal, id_find_animal))
        
    def test_second(self):
        test_case = TestCase()
        id_new_animal = test_case.create_animal('Rabbit')
        id_find_animal = test_case.find_animal(id_new_animal)['id']

        assert id_new_animal == id_find_animal, (
            "[FAILED]: Ids doesnt match {} and {}".format(id_new_animal, id_find_animal))

        test_case.remove_animal(id_new_animal)
        message_find_animal = test_case.find_animal(id_new_animal)['message']

        assert message_find_animal == "Pet not found", (
            "[FAILED]: Animal with the id {} not removed".format(id_new_animal))