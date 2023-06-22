def solution(board, moves):
    answer = 0
    

    stack = []
    for move in moves:
        
        y = 0
        while y != len(board):
            if board[y][move-1]:
                if stack and stack[-1] == board[y][move-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[y][move-1])
                board[y][move-1] = 0
                break
            else:
                y += 1
    
    return answer