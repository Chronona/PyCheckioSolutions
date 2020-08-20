#!/usr/local/bin/checkio --domain=py run replace-last


replace_last = lambda items: [items[-1]] + items[:-1] if len(items) > 0 else items
