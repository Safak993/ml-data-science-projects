import sys
import time
efekt = ["/", "-", "\\", "|"]
# bir yükleme efekti
for i in range(5):
    for j in efekt:
        sys.stdout.write(f"\b{j}")
        sys.stdout.flush() # Tamponu hemen boşalt (yazıyı anında göster)
        time.sleep(0.5)