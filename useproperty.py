#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

#_*_ coding: utf-8 _*_

class Screen:
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,width):
        if not isinstance(width,int):
            raise ValueError('width must be an integer!')
        if width<0:
            raise ValueError('width must greate tan 0!')
        self._width=width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,height):
        if not isinstance(height,int):
            raise ValueError('height must be an integer!')
        if height<0:
            raise ValueError('height must greate tan 0!')
        self._height=height

    @property
    def resolution(self):
        return self._width*self._height
    

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution