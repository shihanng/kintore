local Robot = { name = "" }

Robot.random_char = function()
	return string.char(math.random(65, 65 + 25))
end

Robot.name_generator = function()
	return string.format(
		"%s%s%d%d%d",
		Robot.random_char(),
		Robot.random_char(),
		math.random(0, 9),
		math.random(0, 9),
		math.random(0, 9)
	)
end

Robot.new_name = function()
	local name = Robot.name_generator()

	while Robot.names[name] ~= nil do
		name = Robot.name_generator()
	end

	Robot.names[name] = true
	return name
end

Robot.names = {}

function Robot:reset()
	self.name = Robot.new_name()
end

function Robot:new()
	local obj = {}
	obj.name = Robot.new_name()

	setmetatable(obj, self)
	self.__index = self
	return obj
end

return Robot
