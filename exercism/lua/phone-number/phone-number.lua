local PhoneNumber = { area = "", exchange = "", sub = "", number = "" }

PhoneNumber.__tostring = function(obj)
	return string.format("(%s) %s-%s", obj.area, obj.exchange, obj.sub)
end

function PhoneNumber:areaCode()
	return self.area
end

function PhoneNumber:new(number)
	local obj = {}

	obj.area, obj.exchange, obj.sub = string.match(number, "^[1+(]*([2-9]%d%d)[^%d]*(%d%d%d)[^%d]*(%d%d%d%d)$")
	obj.number = (obj.area or "000") .. (obj.exchange or "000") .. (obj.sub or "0000")

	setmetatable(obj, self)
	self.__index = self
	return obj
end

return PhoneNumber
