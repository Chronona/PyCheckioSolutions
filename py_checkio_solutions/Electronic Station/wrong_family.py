#!/home/user/.local/bin/checkio --domain=py run wrong-family

def is_family(tree):
    for i in range(len(tree)):
      a = tree[i]
      if len(tree) <= 1:
        return True
      elif a[::-1] in tree:
        return False
      else:
        pass

      if len([j for j in tree if a[0] == j[0]]) >= 2:
        continue
      elif len([j for j in tree if a[1] == j[1]]) >= 2:
        return False
      elif len([j for j in tree if a[1] == j[0]]) > 0:
        continue
      elif len([j for j in tree if a[0] == j[1]]) > 0:
        continue
      else:
        return False
    return True


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
