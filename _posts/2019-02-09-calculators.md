---
title: Calculators
layout: post
permalink: /2019/02/09/calculators.html
---

This is a test of simple calculations in html using forms.
These are largely replicates of some of the convenience calculators found
[here](http://bnmr.triumf.ca/?file=Technical_Information).

Simply enter a new value in one of the forms and press ENTER or click outside the box
to update the values.

---

### β-NQR spectrometer magnet current to field converter

<center>
<form>
   <table cellpadding="10" cellspacing="0">
   <tbody>
   <tr>
   <td>
   
   </td>
   <td>
   <b>ILE2A1:HH</b>
   </td>
   </tr>
   <tr>
   <td>
   
   </td>
   <td>
   <i>H</i> (G) = <i>a</i> (G) + <i>b</i> (G/A) × <i>I</i> (A)
   </td>
   </tr>
   <tr>
   <td>
   Current setpoint [<i>I</i>] (A):
   </td>
   <td>
   <input name="I" value="90.292" onchange="H.value = (2.21309 * this.value + 0.17476)" type="text">
   </td>
   </tr>
   <tr>
   <td>
   Magnetic field [<i>H</i>] (G):
   </td>
   <td>
   <input name="H" value="200" onchange="I.value = (this.value - 0.17476 ) / 2.21309" type="text">
   </td>
   </tr>
   </tbody>
   </table>
</form>
</center>

The calibration constants are: _a_ = 0.175 ± 0.046 G and _b_ = 2.2131 ± 0.0019 G/A.


---

### RF bandwidth to pulse duration converter

<center>
<form>
<table cellpadding="10" cellspacing="0">
   <tbody>
      <tr>
      <td>
      
      </td>
      <td>
      <b>ln-sech</b>
      </td>
      <td>
      <b>Hermite</b>
      </td>
      </tr>
      <tr>
      <td>
       
      </td>
      <td>
      <i>t</i><sub>pulse</sub> (ms) × <i>B</i><sub>w</sub> (Hz) = 5 × 10<sup>4</sup>/π
      </td>
      <td>
      <i>t</i><sub>pulse</sub> (ms) × <i>B</i><sub>w</sub> (Hz) = 1764.8
      </td>
      </tr>
      <tr>
      <td>
      Pulse duration [<i>t</i><sub>pulse</sub>] (ms):
      </td>
      <td>
      <input name="Tls" value="79.5816" onchange="Bls.value = 15916.4/( this.value ) " type="text">
      </td>
      <td>
      <input name="Th" value="8.82" onchange="Bh.value = 1764.8/( this.value ) " type="text">
      </td>
      </tr>
      <tr>
      <td>
      Bandwidth [<i>B</i><sub>w</sub>] (Hz):
      </td>
      <td>
      <input name="Bls" value="200"  onchange="Tls.value = 15916.4/( this.value ) " type="text">
      </td>
      <td>
      <input name="Bh" value="200" onchange="Th.value = 1764.8/( this.value ) " type="text">
      </td>
      </tr>
   </tbody>
</table>
</form>
</center>

---

### β-NMR antenna pickup to RF field converter

<center>
<form>
   <table cellpadding="10" cellspacing="0">
   <tbody>
   <tr>
   <td>
   
   </td>
   <td>
   <b><i>H</i><sub>1</sub> field</b>
   </td>
   </tr>
   <tr>
   <td>
   
   </td>
   <td>
   <i>H</i><sub>1</sub> (G) = 39.6 (G MHz/V) × <i>V</i><sub>p-p</sub> (V) / <i>f</i> (MHz)
   </td>
   </tr>
   <tr>
   <td>
   Antenna pickup [<i>V</i><sub>p-p</sub>] (V):
   </td>
   <td>
   <input name="Vpp" value="0.40" onchange="Hrf.value = (39.6 * this.value / 41.27)" type="text">
   </td>
   </tr>
   <tr>
   <td>
   RF frequency [<i>f</i>] (MHz):
   </td>
   <td>
   41.27
   </td>
   </tr>
   <tr>
   <td>
   RF field [<i>H</i><sub>1</sub>] (G):
   </td>
   <td>
   <input name="Hrf" value="0.38" onchange="Vpp.value = (41.27 * this.value / 39.6)" type="text">
   </td>
   </tr>
   </tbody>
   </table>
</form>
</center>

The above expression is accurate to ± 3 %.
