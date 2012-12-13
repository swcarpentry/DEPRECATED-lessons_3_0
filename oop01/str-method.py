import math

# main:start
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%4.2f, %4.2f)' % (self.x, self.y)

if __name__ == '__main__':
    p = Point(3, 4)
    print 'point is', p
# main:end
