from pyscript import display, document

def make_receipt(e):
    iced_mocha = document.getElementById('iced mocha')
    hot_mocha = document.getElementById('hot mocha')
    hot_chocolate = document.getElementById('hot chocolate')
    iced_vanilla = document.getElementById('iced vanilla')
    hot_vanilla = document.getElementById('hot vanilla')

    subtotal = float(iced_mocha.value) * iced_mocha.checked + float(hot_mocha.value) * hot_mocha.checked + float(hot_chocolate.value) * hot_chocolate.checked + float(iced_vanilla.value) * iced_vanilla.checked + float(hot_vanilla.value) * hot_vanilla.checked
    vAT = subtotal * 0.12
    total_cost = subtotal + vAT

    display(f'Your subtotal is ₱{subtotal:.2f}', target='receipt')
    display(f'Your VAT is ₱{vAT:.2f}', target='receipt')
    display(f'Your order costs ₱{total_cost:.2f} in total', target='receipt')