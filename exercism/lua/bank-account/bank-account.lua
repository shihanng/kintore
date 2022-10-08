local BankAccount = { val = 0, is_close = false }

function BankAccount:new()
	local obj = {}
	setmetatable(obj, self)
	self.__index = self
	return obj
end

function BankAccount:balance()
	return self.val
end

function BankAccount:deposit(amount)
	assert(amount > 0)
	assert(not self.is_close)
	self.val = self.val + amount
end

function BankAccount:withdraw(amount)
	assert(amount > 0)
	assert(not self.is_close)
	assert(self.val >= amount)
	self.val = self.val - amount
end

function BankAccount:close()
	self.is_close = true
end

return BankAccount
