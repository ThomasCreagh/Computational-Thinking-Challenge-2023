using Combinatorics

@time begin
    arr = [i for i in range(2, 20)]
    k = 3

    for i in Combinatorics.combinations(arr, k)
        # println(i)
        pass
    end
end