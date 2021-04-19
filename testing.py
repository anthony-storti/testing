import unittest

import System
import User
import Organization


class TestSum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # called one time, at the very beginning
        print('setUpClass()')

        cls.organization = Organization.Organization("Dunder Mifflin", "Scranton PA", "Regional Paper Distributor",
                                                     ["sales", "accounting", "corporate", "warehouse",
                                                      "hr", "management"])

        cls.system = System.System("Accounting Database", "Financial", 3, 2, "accounting", [])

        cls.user_level_5 = User.User('Dwight Shrute', "Assistant to the  Regional Manager", 5,
                                     "Dunder Mifflin", True, [], [])

        cls.user_level_1 = User.User('David Wallace', "CFO", 1,
                                     "Dunder Mifflin", True, [], [])

    def setUp(self):
        # called before every test
        self.user_level_1.set_user_online(True)
        self.user_level_5.set_user_online(True)
        self.system.set_system_license_count(2)
        self.user_level_5.set_available_systems(self.system)
        self.user_level_1.set_available_systems(self.system)

    def tearDown(self):
        # called after every test
        print('tearDown()')
        self.user_level_1.terminate()
        self.user_level_5.terminate()
        self.user_level_1.clear_available_system()
        self.user_level_5.clear_available_system()

    def test_allocate_user_unavailable_system(self):
        """
        Test that a user cannot be allocated a system not available to them
        """
        self.user_level_5.clear_available_system()
        self.user_level_5.allocate_system(self.system.get_system_name())
        result = len(self.user_level_5.get_user_assigned_systems())
        self.assertEqual(result, 0)

    def test_allocate_user_incorrect_clearance(self):
        """
        Test that a user with incorrect clearance will not be assigned system above clearance level
        """
        self.user_level_5.allocate_system(self.system.get_system_name())
        result = len(self.user_level_5.get_user_assigned_systems())
        self.assertEqual(result, 0)

    def test_allocate_deficit_license_count(self):
        """
        Test that a user cannot allocate a system with insufficient licenses
        """
        self.system.set_system_license_count(0)
        self.user_level_1.allocate_system(self.system.get_system_name())
        result = (len(self.user_level_1.get_user_assigned_systems()))
        self.assertEqual(result, 0)

    def test_allocate_user_offline(self):
        """
        Test that a user cannot be allocated a system when offline
        """
        self.user_level_1.set_user_online(False)
        self.user_level_1.allocate_system(self.system.get_system_name())
        result = (len(self.user_level_1.get_user_assigned_systems()))
        self.assertEqual(result, 0)

    def test_allocate_user_correct_clearance_license_online(self):
        """
        Test that a user with correct clearance, online, available systems and system has available licenses
        can be assigned a system
        """
        self.user_level_1.allocate_system(self.system.get_system_name())
        result = len(self.user_level_1.get_user_assigned_systems())
        self.assertEqual(result, 1)

    def test_allocate_user_correct_multiple_allocations_incorrect(self):
        """
        Test that a user with correct clearance, online, available systems and system has available licenses
        can be assigned to a system twice
        """
        self.user_level_1.allocate_system_incorrect(self.system.get_system_name())
        self.user_level_1.allocate_system_incorrect(self.system.get_system_name())
        result = len(self.user_level_1.get_user_assigned_systems())
        self.assertEqual(result, 1)

    def test_allocate_user_correct_multiple_allocations(self):
        """
        Test that a user with correct clearance, online, available systems and system has available licenses
        can be assigned to a system twice
        Bug Fixed - Updated code to check if user has already been assigned the system
        """
        self.user_level_1.allocate_system(self.system.get_system_name())
        self.user_level_1.allocate_system(self.system.get_system_name())
        result = len(self.user_level_1.get_user_assigned_systems())
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()