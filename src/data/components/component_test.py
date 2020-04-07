import unittest

import collider, enemies, bricks


class ComponentTest(unittest.TestCase):

    def setUp(self):
        self.pipe = collider.Pipe(1,2)
        self.brick = bricks.Brick(1,2, 'coin')
        self.step = collider.Step(1,2)
        self.pipe = collider.Pipe(1,2)
        self.goomba = enemies.Goomba(1,2)
        self.koopa = enemies.Koopa(1,2)

    def testPipeCoordinate(self):
        self.assertEqual(self.pipe.rect.x, 1)
        self.assertEqual(self.pipe.rect.y, 2)

    def testStep(self):
        self.assertEqual(self.step.rect.x, 1)
        self.assertEqual(self.step.rect.y, 2)

    def testBrick(self):
        self.assertEqual(self.brick.rect.x, 1)
        self.assertEqual(self.brick.rect.y, 2)
        self.assertEqual(brick.contents, 'coin')
    
    def testEnemies(self):
        self.assertEqual(self.goomba.rect.x, 1)
        self.assertEqual(self.goomba.rect.y, 2)
        self.assertEqual(self.koopa.rect.x, 1)
        self.assertEqual(self.koopa.rect.y, 2)
    
    def testSerialize(self):
        l = [self.pipe, self.brick, self.pipe, self.goomba, self.koopa]
        for item in l:
            data = item.serialize()
            self.assertEqual(data['x'], 1)
            self.assertEqual(data['y'], 2)
        
        brickData = self.brick.serialize()
        self.assertEqual(brickData['contents'], 'coin')

# Example usage
if __name__ == '__main__':
    unittest.main()
