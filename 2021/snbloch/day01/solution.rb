depths = File.readlines('input.txt').map(&:to_i)

curr = nil
deeper = 0
depths.each do |d|
    deeper += 1 if curr != nil && d > curr
    curr = d
end
puts deeper

curr = nil
deeper = 0
i = 0
while i < depths.length - 2 do
    sum = depths[i] + depths[i + 1] + depths[i + 2]
    deeper += 1 if curr != nil && sum > curr
    curr = sum
    i += 1
end
puts deeper