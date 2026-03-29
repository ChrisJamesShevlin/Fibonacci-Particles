<img width="1920" height="1080" alt="fibonacci" src="https://github.com/user-attachments/assets/f116db10-2479-4cd8-8f62-ad6b3f5f4afd" />


---

# 🌻 Generative Study 002 — Fibonacci Particles

This project explores how simple mathematical rules can generate complex visual structure over time.

At its core, the system places particles using a spiral pattern derived from the golden angle:

```python
angle = n * 137.5
radius = 4 * math.sqrt(n)
```

Each frame, a new particle is added to the canvas.

---

## ⚙️ The System

The `draw()` loop runs continuously, and each iteration adds one new particle:

```python
py5.circle(x, y, 8)
```

The background is only set once:

```python
py5.background(0)
```

Nothing is cleared.

The image emerges gradually as particles build on top of each other.

---

## 🧠 What the Code Actually Does

The system is driven by a single variable:

```python
n += 1
```

This counter determines where each new particle is placed.

### 1. Angular Progression

Each particle is rotated slightly from the previous one:

```python
angle = n * 137.5
```

This value (the golden angle) prevents alignment and creates even distribution.

---

### 2. Radial Growth

Distance from the center increases over time:

```python
radius = 4 * math.sqrt(n)
```

Using `sqrt(n)` slows the growth, keeping particles dense near the center and more spaced outward.

---

### 3. Polar → Cartesian Conversion

The spiral is mapped into screen space:

```python
x = cx + radius * math.cos(angle_rad)
y = cy + radius * math.sin(angle_rad)
```

This converts rotation and distance into position.

---

### 4. Colour as Variation

Each particle is assigned a random colour:

```python
py5.fill(py5.random(255), py5.random(255), py5.random(255))
```

The structure is deterministic, but the colour introduces noise.

---

## 🌀 From Code to Behaviour

Although the system is simple, the output is highly structured.

Instead of overlapping randomly:

* particles distribute evenly
* gaps are minimized
* radial “spokes” emerge visually
* density shifts from center to edge

What looks complex is actually the result of:

> a fixed angle + gradual growth + continuous accumulation

---

## 🎛️ Determinism vs Randomness

The positions are completely deterministic.

Every run produces the same spiral layout.

Only the colours change.

This creates an interesting balance:

* **structure** from mathematics
* **variation** from randomness

---

## 💾 Capturing the Output

The current frame can be saved with a key press:

```python
def key_pressed():
    if py5.key == 's':
        py5.save_frame("fibonacci.png")
```

This captures a single moment in an otherwise continuous expansion.

---

## 🧠 Reflection (from a coding perspective)

This project introduced a shift from input-driven drawing to rule-based generation.

There is no interaction.
No mouse input.
No external data.

Only:

* a counter (`n`)
* a mathematical relationship
* and time

Yet the result feels organic.

It demonstrates that:

> complexity can emerge from a single evolving parameter

---

## 🔭 Next Step

Right now, the system generates a single spiral from a fixed center.

Next, I want to extend this into a multi-agent system:

* multiple spirals growing simultaneously
* collision detection between particles
* stopping growth when spirals intersect
* spawning new spirals in empty space

The goal is to move from a single structure to a **self-organising system of competing growth patterns**.

---

*Study 002 — structure emerging from a single rule over time.*
