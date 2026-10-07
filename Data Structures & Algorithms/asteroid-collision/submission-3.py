class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            # Collision is possible only when:
            # stack[-1] is moving right (+)
            # asteroid is moving left (-)
            while stack and stack[-1] > 0 and asteroid < 0:

                if stack[-1] < abs(asteroid):
                    # Right-moving asteroid explodes
                    stack.pop()

                elif stack[-1] == abs(asteroid):
                    # Both explode
                    stack.pop()
                    asteroid = 0
                    break

                else:
                    # Current asteroid explodes
                    asteroid = 0
                    break

            if asteroid != 0:
                stack.append(asteroid)

        return stack