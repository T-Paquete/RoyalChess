class Ability:
    def __init__(self, name):
        self.name = name

    def use(self, piece, board):
        """
        Override this method in subclasses to define the ability's behavior.
        """
        raise NotImplementedError("This ability has no implementation.")
                

class MountDragonAbility(Ability):
    def __init__(self):
        super().__init__("mount_dragon")

    def use(self, wizard, board, dragon, *args, **kwargs):
        from game.piece import MountedWizard
        board.grid[dragon.row][dragon.col] = MountedWizard(wizard.color, dragon.row, dragon.col)
        # i) Only the wizard can mount the dragon
        if wizard.name != "wizard" or dragon.name != "dragon":
            return False  # Invalid usage

        # ii) The dragon must be reachable by the wizard (in wizard's available moves)
        available_moves = []
        for move in wizard.moves:
            available_moves.extend(move.get_possible_moves(wizard, board))
        if (dragon.row, dragon.col) not in available_moves:
            return False  # Dragon not reachable

        # iii) Wizard moves to dragon's square and becomes MountedWizard
        board.grid[wizard.row][wizard.col] = None
        board.grid[dragon.row][dragon.col] = MountedWizard(wizard.color, dragon.row, dragon.col)
        return True  # Successful mounting

class UnmountDragonAbility(Ability):
    def __init__(self):
        super().__init__("unmount_dragon")

    def use(self, mounted_wizard, board):
        from game.piece import Wizard, Dragon
        # i) The dragon stays in the current square
        # ii) The wizard can only unmount to a contiguous empty square
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1), # Up, Down, Left, Right
            (-1, -1), (-1, 1), (1, -1), (1, 1) # Diagonal moves
        ]
        row, col = mounted_wizard.row, mounted_wizard.col
        for delta_row, delta_col in directions:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                if board.grid[new_row][new_col] is None:
                    # iii) Place the wizard in the empty square, dragon stays
                    board.grid[new_row][new_col] = Wizard(mounted_wizard.color, new_row, new_col)
                    board.grid[row][col] = Dragon(mounted_wizard.color, row, col)
                    return True  # Successfully unmounted
        return False  # No available square to unmount


class MountLionAbility(Ability):
    def __init__(self):
        super().__init__("mount_lion")

    def use(self, prince, board, lion):
        from game.piece import MountedPrince
        # i) Only the prince can mount the lion
        if prince.name != "prince" or lion.name != "lion":
            return False  # Invalid usage

        # ii) The lion must be reachable by the prince (in prince's available moves)
        available_moves = []
        for move in prince.moves:
            available_moves.extend(move.get_possible_moves(prince, board))
        if (lion.row, lion.col) not in available_moves:
            return False  # Lion not reachable

        # iii) Prince moves to lion's square and becomes MountedPrince
        board.grid[prince.row][prince.col] = None
        board.grid[lion.row][lion.col] = MountedPrince(prince.color, lion.row, lion.col)
        return True  # Successful mounting

class UnmountLionAbility(Ability):
    def __init__(self):
        super().__init__("unmount_lion")

    def use(self, mounted_prince, board):
        from game.piece import Prince, Lion
        # i) The lion stays in the current square
        # ii) The prince can only unmount to a contiguous empty square
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        row, col = mounted_prince.row, mounted_prince.col
        for delta_row, delta_col in directions:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < board.rows and 0 <= new_col < board.cols:
                if board.grid[new_row][new_col] is None:
                    # iii) Place the prince in the empty square, lion stays
                    board.grid[new_row][new_col] = Prince(mounted_prince.color, new_row, new_col)
                    board.grid[row][col] = Lion(mounted_prince.color, row, col)
                    return True  # Successfully unmounted
        return False  # No available square to unmount


class CombineHatAbility(Ability):
    def __init__(self):
        super().__init__("combine_hat")
        
    def use(self, hat_initiator, board, hat_target):
        from game.piece import GreyHat
        # Check if the pieces have different hat colors
        if not (
            (hat_initiator.name == "white_hat" and hat_target.name == "black_hat") or
            (hat_initiator.name == "black_hat" and hat_target.name == "white_hat")
        ):
            return False
        
        # Check if the target is reachable by the initiator
        available_moves = []
        for move in hat_initiator.moves:
            available_moves.extend(move.get_possible_moves(hat_initiator, board))
        if (hat_target.row, hat_target.col) not in available_moves:
            return False
        
        # Clear initiator's square and place GreyHat on target's square
        board.grid[hat_initiator.row][hat_initiator.col] = None
        board.grid[hat_target.row][hat_target.col] = GreyHat(hat_initiator.color, hat_target.row, hat_target.col)
        
        return True