def two_sum(nums, target):
    num_set = set()  # Conjunto para armazenar números já percorridos

    for i, num in enumerate(nums):
        complement = target - num

        # Verifica se o complemento está no conjunto
        if complement in num_set:
            # Encontrou um par cuja soma é igual ao alvo
            return [nums.index(complement), i]
        
        # Adiciona o número atual ao conjunto
        num_set.add(num)

    # Se nenhum par é encontrado, lança uma exceção ou retorna None, conforme necessário
    raise ValueError("Nenhum par encontrado que some ao alvo")

# Exemplo de uso
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
