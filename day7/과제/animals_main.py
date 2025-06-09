import animals.mammals as am
import animals.birds as ab

dog = am.Dog()
eagle = ab.Eagle()

print(f'개의 다리는 {dog.leg()}개, 얼굴에는 {dog.face()}이 있고, 몸은 {dog.body()}로 덮여있고, {dog.sound()}하고 짖는다. 특징은 {dog.character()}는 것이다.')
print(f'독수리의 다리는 {eagle.leg()}개, 얼굴에는 {eagle.face()}가 있고, 몸은 {eagle.body()}로 덮여있고, {eagle.sound()}하고 운다. 특징은 {eagle.character()}는 것이다.')
