import unittest
from game import new_game, apply_action

class TestMysteryIsland(unittest.TestCase):
    
    def test_new_game_starts_correctly(self):
        """T1: Beach, 5 energy, empty inventory"""
        player = new_game("Ada")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertFalse(player["game_over"])
        self.assertFalse(player["won"])

    def test_invalid_leaves_state_unchanged(self):
        """T2: invalid command leaves state unchanged"""
        player = new_game("Ada")
        original = player.copy()
        original["inventory"] = player["inventory"].copy()
        msg = apply_action(player, "banana")
        self.assertEqual(player["location"], original["location"])
        self.assertEqual(player["energy"], original["energy"])
        self.assertIn("Invalid", msg)

    def test_legal_move_changes_location_and_energy(self):
        """T3"""
        player = new_game("Ada")
        msg = apply_action(player, "north")
        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)

    def test_wrong_direction_no_cost(self):
        """T4"""
        player = new_game("Ada")
        apply_action(player, "south")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_rope_collect_once(self):
        """T5"""
        player = new_game("Ada")
        apply_action(player, "north")
        apply_action(player, "take rope")
        self.assertIn("rope", player["inventory"])
        msg = apply_action(player, "take rope")
        self.assertEqual(player["inventory"].count("rope"), 1)
        self.assertIn("already", msg.lower())

    def test_bridge_needs_rope(self):
        """T6"""
        player = new_game("Ada")
        apply_action(player, "north")
        apply_action(player, "north")  # to Cave
        msg = apply_action(player, "east")
        self.assertEqual(player["location"], "Cave")
        self.assertIn("rope", msg.lower())

    def test_lighthouse_needs_lantern(self):
        """T7"""
        player = new_game("Ada")
        player["location"] = "Old Bridge"
        player["inventory"] = ["rope"]
        msg = apply_action(player, "east")
        self.assertEqual(player["location"], "Old Bridge")
        self.assertIn("lantern", msg.lower())

    def test_win_with_correct_items(self):
        """T8"""
        player = new_game("Ada")
        player["location"] = "Lighthouse"
        player["inventory"] = ["rope", "lantern"]
        player["energy"] = 2
        msg = apply_action(player, "light beacon")
        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])
        self.assertIn("WIN", msg)

    def test_energy_exhaustion_loss(self):
        """T9"""
        player = new_game("Ada")
        player["energy"] = 1
        msg = apply_action(player, "north")
        self.assertTrue(player["game_over"])
        self.assertFalse(player["won"])

    def test_replay_resets(self):
        """T10: new_game gives fresh inventory, not reused list"""
        p1 = new_game("Ada")
        p1["inventory"].append("rope")
        p2 = new_game("Ada")
        self.assertEqual(p2["inventory"], [])
        self.assertIsNot(p1["inventory"], p2["inventory"])

if __name__ == "__main__":
    unittest.main()