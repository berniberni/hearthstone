import tkinter as tk

class Calculator():
    """A class to calculate the total damage output."""

    def __init__(self):
        """Load total damage output attribute."""
        self.total_damage_output = 0
        self.fs_base_dmg = 1
        self.fs_targets = 3
        self.eb_base_dmg = 3
        self.eb_targets = 1
        self.sc_base_dmg = 2
        self.sc_targets = 2

    def fetch_input_values(self, entries):
        """Get the label-text pairs."""
        input_dict = {}
        for label, value in entries.items():
            if value.get():
                input_dict[label] = value.get()
            else:
                input_dict[label] = 0
        return input_dict

    def get_spell_damage_output(self, base_damage, targets, spell_damage,
            multi_factor, spell_number):
        """Calculate the damage portion of a given spell."""
        damage = ((base_damage + spell_damage) * targets *
            multi_factor * spell_number)
        return damage

    def get_ls_taunt_flag(self, entry_input):
        """Get the flag for life steal and enemy taunt."""
        try:
            flag = entry_input.lower().startswith('y')
        except AttributeError:
            flag = False
        return flag

    def get_hero_damage_output(self, hero_attack, ls_flag, taunt_flag):
        """Calculate the damage portion of the hero."""
        if ls_flag and not taunt_flag:
            damage = hero_attack * 2
        elif ls_flag or not taunt_flag:
            damage = hero_attack
        else:
            damage = 0
        return damage

    def get_minion_damage_output(self, board_attack, taunt_flag):
        """Calculate the minion damage portion."""
        if not taunt_flag:
            damage = board_attack
        else:
            damage = 0
        return damage

    def update_total_damage(self, entries):
        """
        Update the total damage output possible 
        based on the given information.
        """
        # Prepare input values to calculate total output damage.
        input_dict = self.fetch_input_values(entries)
        spell_damage = int(input_dict["Spell Damage"])
        multi_factor = 2 ** int(input_dict["Mo'arg Artificer"])
        felscream_number = int(input_dict["Felscream Blast"])
        eye_beam_number = int(input_dict["Eye Beam"])
        soul_cleave_number = int(input_dict["Soul Cleave"])
        hero_attack = int(input_dict["Hero Attack"])
        life_steal = input_dict["Life Steal? (y/n)"]
        enemy_taunt = input_dict["Taunt in the way? (y/n)"]
        board_attack = int(input_dict["Board attack"])

        # Calculate the damage portion of each spell.
        felscream_damage = self.get_spell_damage_output(self.fs_base_dmg,
            self.fs_targets, spell_damage, multi_factor, felscream_number)
        eye_beam_damage = self.get_spell_damage_output(self.eb_base_dmg,
            self.eb_targets, spell_damage, multi_factor, eye_beam_number)
        soul_cleave_damage = self.get_spell_damage_output(self.sc_base_dmg,
            self.sc_targets, spell_damage, multi_factor, soul_cleave_number)

        # Get life steal and taunt flags.
        ls_flag = self.get_ls_taunt_flag(life_steal)
        taunt_flag = self.get_ls_taunt_flag(enemy_taunt)
        # Calculate hero and board damage.
        hero_damage = self.get_hero_damage_output(hero_attack, ls_flag,
            taunt_flag)
        minion_damage = self.get_minion_damage_output(board_attack,
            taunt_flag)
        
        # Calculate total damage output and update the label.
        total_damage = (felscream_damage + eye_beam_damage +
            soul_cleave_damage + hero_damage + minion_damage)
        self.total_damage_output = total_damage