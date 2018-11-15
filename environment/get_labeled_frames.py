import random
import numpy as np

SCREEN_SIZE = {'width' : 80, 'height' : 80}
BG_COLOR = [255, 255, 255]

TARGET_SIZE = .75  # fraction of screen to fill

GRID = {'size' : 64, 'step' : 8}

FIXATION_SIZE = .1
FIXATION_COLOR = [255, 0, 0] # RGB
CENTER = [.5, .5]
BUTTON_SIZE = 0.1
END_STUDY_BUTTON_SIZE = .09375

ALLOW_TRANSLATION = True

# These are RGB values, they have a fixed luminance in HSL space.
COLORS = [
    [255, 0, 0],
    [255, 191, 0],
    [127, 255, 0],
    [0, 255, 255],
    [0, 63, 255],
    [127, 0, 255],
    [255, 0, 191]
]

ALL_OPTO_TYPES = ['E', 'Square']
ORIENTATIONS = ['left', 'right', 'up', 'down']
DOMAINS = [
      'E_ALL',
#       'E_COLOR',
#       'E_ORIENTATION',
#       'SQUARE_COLOR',
      'ALL'
  ]



def get_array_median(array):
  if array.shape % 2 == 0:
    return array[np.ceil(array.shape/2)]
  else:
    return (array[np.floor(array.shape/2)]+array[np.ceil(array.shape/2)])/2

def get_size_in_pixels(screen_size, size):
  return {'width': np.floor(size*screen_size.width),
      'height': np.floor(size*screen_size.height)}

def get_random_coords(limit, step):
  full_domain = np.range(np.floor(step/2), limit, step)
  grid_center = get_array_median(full_domain)
  invalid_domain = [-2,-1,1,2]
  x = np.random.choice(full_domain)[0]
  y = np.random.choice(full_domain)[0]
  while (x in invalid_domain) and (y in invalid_domain):
    x = np.random.choice(full_domain)[0]
    y = np.random.choice(full_domain)[0]
  return x, y

class data_generator(object):
  def ___init__():
    self.setup_images()
    self.setup_grid()
    self.setSize = 2
    self.allowTranslation = True

  def setup_images():

      h = BUTTON_SIZE * SCREEN_SIZE.height
      w = BUTTON_SIZE * SCREEN_SIZE.width

      self.images['greenImage'] = np.ones((h, w, 3))
      self.images['greenImage'][:, :, 0] = np.ones((h, w)) * 100
      self.images['greenImage'][:, :, 1] = np.ones((h, w)) *255
      self.images['greenImage'][:, :, 2] = np.ones((h, w)) *100

      self.images['redImage'] = np.zeros((h, w, 3))
      self.images['redImage'][:,:,0] = np.ones((h,w)) *255
      self.images['redImage'][:,:,1] = np.ones((h,w)) *100
      self.images['redImage'][:,:,2] = np.ones((h,w)) *100

      self.images['blackImage'] = np.zeros((h, w, 3))
      self.images['whiteImage'] = np.ones((h, w, 3)) * 255

      self.target_pixels = get_size_in_pixels(SCREEN_SIZE, TARGET_SIZE)
      self.target = np.ones((target_pixels.height, target_pixels.width, 3))

      # create self-paced endStudyPhase button image
      # borderSize = (h + w) / 8
      # TURQUOISE = [59, 165, 170]
      # images['turquoiseBox'] = np.zeros((h, w, 3))
      # borderFill(self.images.turquoiseBox, h, w, borderSize, TURQUOISE)

      # self.images.turquoiseImage = tensor.ByteTensor(h, w, 3)
      # for i in range(3):
      #   images.turquoiseImage:select(3, i):fill(TURQUOISE[i])

  def setup_grid():
    self.grid_limit = GRID.size-GRID.step
    self.grid_step = GRID.step
    self.target_pixels_size = {
        'width' : TARGET_SIZE * SCREEN_SIZE.width,
        'height' : TARGET_SIZE * SCREEN_SIZE.height
      }
    self._hFactor = target_pixels_size.width / GRID.size
    self._vFactor = target_pixels_sixe.height / GRID.size

  def _drawSquare(location, color):
    for i in range(len(color)):
      self._array[location.bottom:location.top,
          location.left:location.right,i] = color[i]

  def _drawE(location, color, orientation):
    height = location.top - location.bottom
    width = location.right - location.left

    twentyPercentY = np.floor(.5 + 0.2 * height) + location.bottom
    fortyPercentY = np.floor(.5 + 0.4 * height) + location.bottom
    sixtyPercentY = np.floor(.5 + 0.6 * height) + location.bottom
    eightyPercentY = np.floor(.5 + 0.8 * height) + location.bottom

    twentyPercentX = np.floor(.5 + 0.2 * width) + location.left
    fortyPercentX = np.floor(.5 + 0.4 * width) + location.left
    sixtyPercentX = np.floor(.5 + 0.6 * width) + location.left
    eightyPercentX = np.floor(.5 + 0.8 * width) + location.left

    # fill with solid color
    self._drawSquare(location, color)

    # block out notches in the E by filling with background color
    if orientation == 'right':
      self._array[twentyPercentY: fortyPercentY,
          fortyPercentX: location.right,: ] = BG_COLOR
      self._array[sixtyPercentY: eightyPercentY,
          fortyPercentX: location.right,: ] = BG_COLOR
    elif orientation == 'left':
      self._array[twentyPercentY: fortyPercentY,
          location.left:sixtyPercentX, : ] = BG_COLOR
      self._array[sixtyPercentY: eightyPercentY,
          location.left:sixtyPercentX, : ] = BG_COLOR
    elif orientation == 'up':
      self._array[sixtyPercentY: location.top,
          twentyPercentX:fortyPercentX,: ] = BG_COLOR
      self._array[sixtyPercentY: location.top,
          sixtyPercentX: eightyPercentX,: ] = BG_COLOR
    elif orientation == 'down':
      self._array[location.bottom:fortyPercentY,
          twentyPercentX:fortyPercentX,: ] = BG_COLOR
      self._array[location.bottom:fortyPercentY,
          sixtyPercentX: eightyPercentX,: ] = BG_COLOR 

  def drawObject(opt):
    if opt.optotype == 'Square':
      self._drawSquare(opt.location, opt.color)
    elif opt.optotype == 'E':
      self._drawE(opt.location, opt.color, opt.orientation)


  def getStudyArrayData():
    self.domainType = random.choice(self.domains)
    domain = self.getDomain(self.domainType)

    studyArrayData = {
        'location' : {},
        'color' : {},
        'colorId' : {},
        'optotype' : {},
        'orientation' : {}
    }

    # -- iterate over objects in the study array
    self._currentStudyLocationsSet = {}
    for i in range(self.setSize):
      # -- generate random location, color, optotype, and orientation
      location = getRandomCoordinates(self._gridLimit, self._gridStep)
      color = random.choose(domain.colors)
      index = domain.colors.index(color)
      colorId = domain.colorIds[index]
      optotype = random.choose(domain.optotypes)
      orientation = random.choose(domain.orientations)

      # -- make sure the random location was not already used
      while location in self._currentStudyLocationsSet:
        location = getRandomCoordinates(self._gridLimit, self._gridStep)
      self._currentStudyLocationsSet.append(location)

      studyArray = {
        'location' : location,
        'color' : color,
        'colorId' : colorId,
        'optotype' : optotype,
        'orientation' :orientation
      }
      studyArrayData.append(studyArray)

    return studyArrayData

  def getDomain(domainType):
    if domainType == 'E_ALL':
      return {
          'optotypes' : ['E'],
          'colors' : COLORS,
          'colorIds' : list(range(1, len(COLORS))),
          'orientations' : ORIENTATIONS
      }
    elif domainType == 'ALL':
       return {
          'optotypes' : ALL_OPTO_TYPES,
          'colors' : COLORS,
          'colorIds' : list(range(1, len(COLORS))),
          'orientations' : ORIENTATIONS
      }
    # elseif domainType == 'E_COLOR' then
    #   local fixedOrientation, _ = psychlab_helpers.randomFrom(ORIENTATIONS)
    #   return {
    #       optotypes = {'E'},
    #       colors = kwargs.colors,
    #       colorIds = psychlab_helpers.range(1, #kwargs.colors),
    #       orientations = {fixedOrientation}
    #   }
    # elseif domainType == 'E_ORIENTATION' then
    #   local fixedColor, fixedColorId = psychlab_helpers.randomFrom(kwargs.colors)
    #   return {
    #       optotypes = {'E'},
    #       colors = {fixedColor},
    #       colorIds = {fixedColorId},
    #       orientations = ORIENTATIONS
    #   }
    # elseif domainType == 'SQUARE_COLOR' then
    #   return {
    #       optotypes = {'Square'},
    #       colors = kwargs.colors,
    #       colorIds = psychlab_helpers.range(1, #kwargs.colors),
    #       orientations = ORIENTATIONS, -- orientation does nothing for a square
    #   }
    # elseif domainType == 'ALL' then
    #   return {
    #       optotypes = ALL_OPTO_TYPES,
    #       colors = kwargs.colors,
    #       colorIds = psychlab_helpers.range(1, #kwargs.colors),
    #       orientations = ORIENTATIONS
    #   }

  def getLegalTransforms(domainType, optotype):
    legalTransforms = []
    if domainType == 'E_ALL':
      legalTransforms = ['COLOR', 'ORIENTATION']
    # elseif domainType == 'E_COLOR' then
    #   legalTransforms = {'COLOR'}
    # elseif domainType == 'E_ORIENTATION' then
    #   legalTransforms = {'ORIENTATION'}
    # elseif domainType == 'SQUARE_COLOR' then
    #   legalTransforms = {'COLOR'}
    elif domainType == 'ALL':
      if optotype == 'E':
        legalTransforms = ['OPTOTYPE', 'COLOR', 'ORIENTATION']
      elif optotype == 'Square':
        legalTransforms = ['OPTOTYPE', 'COLOR']

    if self.allowTranslation:
      legalTransforms.append('TRANSLATION')

    return legalTransforms

  def getTestArray(studyArrayData):
    testArrayData = studyArrayData.copy()
    isNew = np.random.uniform(0, 1) > 0

    if not isNew:
      self.transform = 'NONE'
    else:
      # -- select an object to change
      changedObjectIndex = np.random.randint(1, len(testArrayData.location))

      # -- select a transformation to apply
      legalTransforms = self.getLegalTransforms(
          self.domainType,
          testArrayData.optotype[changedObjectIndex]
      )
      self.transform = random.choose(
        legalTransforms)

      # -- apply the transformation
      if self.transform == 'COLOR':
        # -- make sure the random color is not the one that was already used
        newColor  = random.choose(COLORS)
        newColorId = COLORS.index(newColor)
        while newColor == studyArrayData.color[changedObjectIndex]:
          newColor  = random.choose(COLORS)
          newColorId = COLORS.index(newColor) 
        testArrayData.color[changedObjectIndex] = newColor
        testArrayData.colorId[changedObjectIndex] = newColorId
      elif self.transform == 'ORIENTATION':
        # -- make sure the random orientation is not the one that was already used
        newOrientation = random.choose(ORIENTATIONS)
        while newOrientation == studyArrayData.orientation[changedObjectIndex]:
          newOrientation = random.choose(ORIENTATIONS) 

        testArrayData.orientation[changedObjectIndex] = newOrientation

      elif self.transform == 'OPTOTYPE':
        if testArrayData.optotype[changedObjectIndex] == 'E':
          testArrayData.optotype[changedObjectIndex] = 'Square'
        elif testArrayData.optotype[changedObjectIndex] == 'Square':
          testArrayData.optotype[changedObjectIndex] = 'E'

      elif self.transform == 'TRANSLATION':
        # -- make sure the random location is not on top of another object
        newLocation = getRandomCoordinates(self._gridLimit,
          self._gridStep)
        while newLocation in self._currentStudyLocationsSet:
          newLocation = getRandomCoordinates(self._gridLimit, self._gridStep)

        testArrayData.location[changedObjectIndex] = newLocation
    return testArrayData, isNew

  def renderArray(arrayData):
    if not self._array:
      self._array = np.zeros(self.target_pixels_size.height,
                             self.target_pixels_size.width,
                                      3)
    self._array = BG_COLOR[0]

    # -- draw objects
    for i in range(len(arrayData.location)):
      location = {
          'left' : arrayData.location[i][1] * self._hFactor,
          'right' : (arrayData.location[i][1] + GRID.step) * self._hFactor,
          'bottom' : arrayData.location[i][2] * self._vFactor,
          'top' : (arrayData.location[i][2] + GRID.step) *
            self._vFactor,
      }

      self.drawObject(location = location,
                      color = arrayData.color[i],
                      optotype = arrayData.optotype[i],
                      orientation = arrayData.orientation[i])

    return self._array

