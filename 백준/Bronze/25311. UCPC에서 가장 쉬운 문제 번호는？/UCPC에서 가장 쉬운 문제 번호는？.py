import unittest
def sol(y):
    return 'A'
class SolTest(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(sol(2018),'A')
        self.assertEqual(sol(2019), 'A')
        self.assertEqual(sol(2020), 'A')
        self.assertEqual(sol(2021), 'A')
if __name__ == '__main__':
    #unittest.main()
    y = int(input())
    print(sol(y))