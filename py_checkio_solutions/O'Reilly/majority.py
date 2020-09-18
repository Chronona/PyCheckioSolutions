#!/usr/local/bin/checkio --domain=py run majority


is_majority = lambda items: len([i for i in items if i is True]) > len([i for i in items if i is False])

