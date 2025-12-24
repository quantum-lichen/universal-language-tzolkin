# 🔢 Complete Mathematical Formulas

**All formulas used in Universal Language & Tzolk'in Cryptography**

---

## 1. Perfect Numbers

### Definition
$$\sigma(n) = 2n$$

Where σ(n) is the sum of all divisors of n:
$$\sigma(n) = \sum_{d|n} d$$

### Euclid-Euler Formula
$$N = 2^{p-1} \times (2^p - 1)$$

Where:
- p is prime
- 2^p - 1 is also prime (Mersenne prime)

### First Perfect Numbers
- N₁ = 2¹(2² - 1) = 2 × 3 = **6**
- N₂ = 2²(2³ - 1) = 4 × 7 = **28**
- N₃ = 2⁴(2⁵ - 1) = 16 × 31 = **496**
- N₄ = 2⁶(2⁷ - 1) = 64 × 127 = **8128**

---

## 2. Tzolk'in Calendar

### Basic Structure
$$T = 13 \times 20 = 260 \text{ days}$$

### Position Calculation
Given day d since epoch:
$$\text{day\_number} = (d \bmod 260) + 1$$
$$\text{trecena} = ((d-1) \bmod 13) + 1$$
$$\text{veintena} = ((d-1) \bmod 20) + 1$$

### Calendar Round
$$\text{LCM}(260, 365) = \frac{260 \times 365}{\text{GCD}(260, 365)} = 18,980 \text{ days}$$

---

## 3. Cryptographic Key Generation

### Seed Calculation
$$\text{seed} = \text{day\_number} \times 10^6 + \text{trecena} \times 10^3 + \text{veintena}$$

### Mixing with φ
$$\text{seed'} = (\text{seed} \times \lfloor \varphi \times 10^{15} \rfloor) \bmod 2^{64}$$

Where φ = 1.618033988749895...

### Key Generation
$$K = \text{SHA-256}(\text{seed'})$$

For longer keys:
$$K_n = K_0 \| \text{SHA-256}(K_0) \| \text{SHA-256}(\text{SHA-256}(K_0)) \| ...$$

---

## 4. One-Time Pad Encryption

### Encryption
$$C = M \oplus K$$

Where:
- C = ciphertext
- M = message
- K = key
- ⊕ = XOR operation

### Decryption
$$M = C \oplus K$$

(XOR is its own inverse)

---

## 5. Shannon's Perfect Secrecy

### Entropy Condition
$$H(M|C) = H(M)$$

Meaning: observing C gives zero information about M.

### Formal Definition
$$P(M=m|C=c) = P(M=m) \quad \forall m,c$$

---

## 6. Prime Number Formulas

### Prime Counting Function
$$\pi(x) \approx \frac{x}{\ln(x)}$$

### Mersenne Prime Test (Lucas-Lehmer)
For M_p = 2^p - 1, define sequence:
$$S_0 = 4$$
$$S_{i+1} = S_i^2 - 2$$

M_p is prime ⟺ S_{p-2} ≡ 0 (mod M_p)

---

## 7. Universal Constants

### Golden Ratio
$$\varphi = \frac{1 + \sqrt{5}}{2} = 1.618033988749895...$$

Property:
$$\varphi^2 = \varphi + 1$$

### Pi
$$\pi = \frac{C}{d} = 3.14159265358979...$$

Where C = circumference, d = diameter

### Euler's Number
$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = 2.71828182845905...$$

---

## 8. Base-28 Encoding

### Character Mapping
$$c_i \in [1, 28]$$

Where:
- 1-26: A-Z
- 27: SPACE
- 28: PUNCTUATION

### Message Encoding
$$M = \{c_1, c_2, ..., c_n\}$$

Transmission:
$$T = [c_1]_{28} \cdot p_1 \cdot [c_2]_{28} \cdot p_2 \cdot ... \cdot [c_n]_{28} \cdot M_{31}$$

Where:
- [x]_28: x pulses in base-28
- p_i: prime gap separator
- M_31: Mersenne prime terminal

---

## 9. Astronomical Calculations

### Solar Position (simplified)
$$\text{azimuth} = \arctan\left(\frac{\sin(H)}{\cos(H)\sin(L) - \tan(\delta)\cos(L)}\right)$$

Where:
- H = hour angle
- L = latitude
- δ = declination

### Day of Year
$$\text{DOY} = \lfloor \frac{275M}{9} \rfloor - \lfloor \frac{M+9}{12} \rfloor \times (1 + \lfloor \frac{Y-4\lfloor Y/4 \rfloor + 2}{3} \rfloor) + D - 30$$

Where M = month, D = day, Y = year

---

## 10. Information Theory

### Shannon Entropy
$$H(X) = -\sum_{i=1}^n P(x_i) \log_2 P(x_i)$$

### Mutual Information
$$I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$$

### Channel Capacity
$$C = \max_{P(x)} I(X;Y)$$

---

## 11. Security Metrics

### Key Space
$$|K| = 2^{256} \text{ (SHA-256 output)}$$

### Brute Force Complexity (Classical)
$$O(2^{256})$$

### Brute Force Complexity (Quantum - Grover)
$$O(2^{128})$$

### Birthday Attack Threshold
$$n \approx \sqrt{2^{256}} = 2^{128}$$

---

## 12. Perfect Number Properties

### Binary Representation
$$N_k = 2^{p-1}(2^p - 1) = \underbrace{111...1}_{p} \underbrace{000...0}_{p-1}_2$$

Example: 496 = 111110000₂

### Sum of Cubes (Odd Numbers)
$$496 = 1^3 + 3^3 + 5^3 + 7^3$$

General formula:
$$N_k = \sum_{i=1}^{2^{(p-1)/2}} (2i-1)^3$$

### Triangular Number Property
$$N_k = T_{2^p - 1}$$

Where T_n is the n-th triangular number:
$$T_n = \frac{n(n+1)}{2}$$

---

## 13. Complexity Analysis

### Time Complexity

| Operation | Complexity |
|-----------|-----------|
| Position calculation | O(1) |
| Key generation | O(1) |
| Encryption | O(n) |
| Decryption | O(n) |
| Perfect number verification | O(√n) |

### Space Complexity

| Data Structure | Space |
|----------------|-------|
| Key storage | O(1) (generated on-demand) |
| Message buffer | O(n) |
| Total system | O(n) |

---

## 14. Probability and Statistics

### False Positive Rate (Linguistic)
For n-character English message:
$$P_{\text{false}} \approx 2^{-1.5n}$$

(English entropy ≈ 1.5 bits/char)

### Collision Probability (SHA-256)
$$P_{\text{collision}} \approx \frac{k^2}{2 \times 2^{256}}$$

For k hashes (birthday paradox)

---

## 15. Astronomical Cycles

### Precession Period
$$T_{\text{prec}} = 25,920 \text{ years}$$

### Tzolk'in-Precession Relation
$$\frac{25,920 \text{ years}}{260 \text{ days}} \times 365.25 = 36,450$$

(Approximately)

### Venus Synodic Period
$$T_{\text{Venus}} = 584 \text{ days}$$

$$\frac{584 \times 5}{260} \approx 11.23$$

---

## 16. Error Correction

### Hamming Distance
$$d(x,y) = |\{i : x_i \neq y_i\}|$$

### Minimum Distance Bound
For detection of t errors:
$$d_{\min} \geq t + 1$$

For correction of t errors:
$$d_{\min} \geq 2t + 1$$

---

## 17. Quantum Computing Resistance

### Grover's Algorithm Speedup
$$T_{\text{quantum}} = O(\sqrt{T_{\text{classical}}})$$

For search space N:
$$T_{\text{classical}} = O(N)$$
$$T_{\text{quantum}} = O(\sqrt{N})$$

For N = 2^256:
$$T_{\text{quantum}} = O(2^{128})$$ (still infeasible)

---

## 18. Implementation Constants

```python
PHI = 1.618033988749895
PI = 3.141592653589793
E = 2.718281828459045
PHI_INT = int(PHI * 10**15)  # 1618033988749895

EPOCH = datetime(year=-3113, month=8, day=11)  # Mayan Long Count start
TZOLKIN_CYCLE = 260
TRECENA = 13
VEINTENA = 20
```

---

## 19. Validation Formulas

### Perfect Number Check
```python
def is_perfect(n):
    return sum(d for d in range(1, n) if n % d == 0) == n
```

### Key Uniqueness Verification
$$\forall i \neq j \in [1, 260]: K_i \neq K_j$$

(All 260 keys must be distinct)

---

## 20. Performance Metrics

### Throughput
$$\text{Throughput} = \frac{\text{Bytes processed}}{\text{Time elapsed}}$$

### Latency
$$\text{Latency} = t_{\text{enc}} + t_{\text{trans}} + t_{\text{dec}}$$

### Efficiency
$$\text{Efficiency} = \frac{\text{Payload size}}{\text{Total transmission size}}$$

---

**End of Formulas**

For implementation details, see [src/tzolkin_crypto.py](src/tzolkin_crypto.py)
