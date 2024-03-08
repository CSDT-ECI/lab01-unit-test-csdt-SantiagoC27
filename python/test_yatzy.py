from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


# def test_demo():
#         expected = 15
#         actual = 15
#         assert expected == actual

def test_Chance_SumAllDice():
        excected1 = 14
        expected2 = 21

        result1 = Yatzy.chance(1,1,3,3,6)
        result2 = Yatzy.chance(4,5,5,6,1)

        assert excected1 == result1
        assert expected2 == result2

def test_Yatzy_AllDiceSame():
        excected1 = 50
        expected2 = 0

        result1 = Yatzy.yatzy([1,1,1,1,1])
        result2 = Yatzy.yatzy([1,1,1,2,1])

        assert excected1 == result1
        assert expected2 == result2

def test_Ones_SumOnlyOneDice():
        excected1 = 2

        result1 = Yatzy.ones(1,1,3,3,6)

        assert excected1 == result1

def test_Twos_SumOnlyTwoDice():
        excected1 = 6

        result1 = Yatzy.twos(1,2,2,2,6)

        assert excected1 == result1

def test_Thres_SumOnlyThreDice():
        excected1 = 6

        result1 = Yatzy.threes(1,1,3,3,6)

        assert excected1 == result1

def test_Four_SumOnlyFourDice():
        excected1 = 12
        yt = Yatzy(4,1,4,4,6)
        result1 = yt.fours()

        assert excected1 == result1

def test_Five_SumOnlyFiveDice():
        excected1 = 10
        yt = Yatzy(1,5,3,5,6)
        result1 = yt.fives()

        assert excected1 == result1

def test_Six_SumOnlySixDice():
        excected1 = 24
        yt = Yatzy(6,6,6,3,6)
        result1 = yt.sixes()

        assert excected1 == result1

def test_CrazyChance_MultipliSum():
        expected1 = 48
        expected2 = 30
        expected3 = 52

        result1 = Yatzy.crazyChance([2,4,6,2,2])
        result2 = Yatzy.crazyChance([1,1,3,5,5])
        result3 = Yatzy.crazyChance([2,4,3,5,6])

        assert expected1 == result1
        assert expected2 == result2
        assert expected3 == result3