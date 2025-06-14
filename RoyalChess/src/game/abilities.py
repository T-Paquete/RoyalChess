from piece import *

class Ability:
    def __init__(self, name):
        self.name = name

    def use(self, piece, board, **kwargs):
        """
        Override this method in subclasses to define the ability's behavior.
        """
        raise NotImplementedError("This ability has no implementation.")

# Example: Wizard's ability to mount a dragon
class MountDragonAbility(Ability):
    def __init__(self):
        super().__init__("mount_dragon")

    def use(self, wizard, board, dragon):
        # Remove wizard and dragon from their positions
        board.grid[wizard.row][wizard.col] = None
        board.grid[dragon.row][dragon.col] = MountedWizard(wizard.color, dragon.row, dragon.col)