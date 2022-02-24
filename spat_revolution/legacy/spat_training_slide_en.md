autoscale: true
theme: Sketchnote, 2
slidenumbers: true
autoscale: true
footer: FLUX:: Spat Revolution training, All writing is protected under copyright ©2020 FLUX SOFTWARE ENGINEERING



# ![](include/favicon-32x32.png ':class=img-title') FLUX:: IRCAM Spat Revolution

## Professional Certification guide

**Written by:** Jean-Loup Pecquais, Hugo Larin, Nicolas Erard and Christian Vogel 

**With contributions:** from Gaël Martinet, Markus Noisterning, Oliver Warusfel, Philippe Langlois, Thibaut Carpentier, Vincent Carlier.


---

## Legal Information


First edition of Flux:: IRCAM Spat Revolution Professional certification
<br>
All writing is protected under copyright ©2020 FLUX SOFTWARE ENGINEERING

---

	All trademarks and the logos are copyright protected.
> 

```
Flux:: Spat Revolution is published by:
FLUX SOFTWARE ENGINEERING
2, Rue de la Chasse
45000 ORLEANS
R.C.S 431 616 770 ORLEANS
```
> 

	IRCAM Tools SPAT Copyright 2020 FLUX SOFTWARE ENGINEERING and IRCAM.   

	SPAT Revolution Copyright 2020 FLUX SOFTWARE ENGINEERING and IRCAM. 

	All rights reserved.

---

## Objectives

* Explore advanced techniques and principles for creating high-quality spatial audio productions.
<br>
* Deepen your knowledge of 3D audio technologies (HOA, WFS, binaural, …), auditory spatial perception, room acoustics, and reverberation processing.
<br>
* Learn to design and implement massive multi-channel audio systems for real-time 3D audio productions.
<br>
* Master Spat Revolution and its integration into your workflows for studio and/or live productions (software configuration, multichannel audio pipeline, communication with third-party applications or peripherals, basic troubleshooting).

---

## Target Audience

* Participants should be sound designers, audio engineers, or sound system engineers with interest in multi-channel audio.


---

## Prerequisites

* Basic understanding of spatial audio technologies.
<br>
* Basic understanding, and experience using DAW (Pro Tools, Ableton Live, Reaper, Logic Pro, Nuendo, etc.) is recommended.
<br>
* Understanding of complex multi-channel workflows, audio systems, and audio formats is recommended (multichannel i/o peripherals, hardware protocols, system design and engineering, sound diffusion and audio mixing).


---

## Configuration

 
* Each participant must bring his/her own portable laptop computer running macOS High Sierra 10.13 , Mojave 10.14 or  Catalina 10.15 on Windows 10 Professional 64Bit
<br>
* Computers must have an operational DAW software of choice running  ( with a multi-track audio demo session … FLUX to provide multitrack sessions and audio files????) 
<br>
* Each participant must provide an audio interface with built in headphone output together with personal headphone
<br>
* Each participant to be equipped with a Spat Revolution software license and be running the last public version
<br>
* Spat Revolution suite of software to be installed (Spat Revolution application, Spat Send PI, Spat Return PI, Spat Room PI)


---

## Professional Certification Modules

1. Spatial Audio Concepts
1. Spat Revolution for Spatial Audio Productions.
1. Spat Revolution Integration.
1. Third-Party, Examples, and Case Studies.                                                          

---

# ![](include/favicon-32x32.png ':class=img-title') Spatial audio concepts

[.hide-footer]

---

# 1. Spatial Audio Concepts

* 1.1. Historical overview
* 1.2. Spatial audio production ecosystem
* 1.3. Auditory spatial perception                 
* 1.4. Advanced spatial audio techniques         
* 1.5. IRCAM Spat architecture


---

## 1.1 Historical Overview
 
* 1.1.1. Spatial audio in music
* 1.1.2. Historical milestones
* 1.1.3. Some examples  


---

## 1.2 Spatial Audio Production; Ecosystem 

* 1.2.1. Application domains
* 1.2.2. Associated tools
* 1.2.3. Spat Revolution and production workflows


---

## 1.3 Auditory Spatial Perception

* 1.3.1. 	(Theoretical background on) Sound localization
* 1.3.2. 	(Theoretical background on) Room acoustics perception


---

## 1.4. Advanced Spatial Audio Techniques
 
* 1.4.1. General principles of sound spatialization
* 1.4.2. 2D and 3D Panning methods
* 1.4.3. Binaural audio
* 1.4.4. Wave Field Synthesis (WFS)
* 1.4.5. Higher Order Ambisonics (HOA)
* 1.4.6. Other spatial audio methods


---

## 1.5. IRCAM Spat Architecture
 
* 1.5.1. IRCAM Spat architecture
* 1.5.2. Internal signal processing structure
* 1.5.3. Room and source control
* 1.5.4. Room acoustic simulation


---


# ![](include/favicon-32x32.png ':class=img-title') Spat Revolution for spatial audio productions


**Presented by: Hugo Larin**

[FLUX:: Immersive](https://www.fluximmersive.com "")

   
---

# 2. Spat Revolution for spatial audio productions#

* 2.1. Getting started and configuration

* 2.2. Immersive workflow introduction

* 2.3. Implementation of spatialization techniques                   

* 2.4. Room effects and the source objects
        
* 2.5. Hands-On exercises - Spatial Audio Productions**


---

## 2.1.1. Introduction to basic concepts
## Welcome to Spat Revolution
[.hide-footer]

---

![](include/Spat_Screen_Shot.png ':class=img-title')

### ![](include/favicon-32x32.png ':class=img-title')What is Spat Revolution?
[.hide-footer]

^ 
<br>
**'Spat'** is short for Spatialisateur in French. It is a real-time audio library that allows composers, sound artists, performers and sound engineers to control the localisation of sound sources in virtual and real 3D auditory spaces.
Spat Revolution wraps the 'Spat' processing library in a luxurious and characteristic graphic environment to help visualise many aspects of a spatial audio composition in realtime. This graphic interface allows sound mixes to be composed as interactive spatial models existing in Virtual Room. 
<br>
<br>
High definition graphic displays like the unique Nebula analyser for example, can simulate how sound sources localise their direct sound over different speaker setups. 
In addition, Spat contains a powerful multichannel reverberation engine which can be applied to design and add a sense of auditory space in studio mixes and realtime on location.

---

### Spat Revolution's Heritage

* Flux:: the IRCAM audio software development partner since 2011
<br>
* IRCAM (Institute for Research and Coordination Acoustic/Music) 
<br>
* +30 years of research by the Acoustic and Cognitive Spaces Team at the French IRCAM institute  
<br>

^ 
<br>
Behind _Spat Revolution_ is the partnership of FLUX:: and IRCAM in Paris, France. Founded in 1977, IRCAM is one of the world’s leading public research institutes in the fields of musical expression, science of music, sound and acoustics.
<br>
<br>
The first result of this partnership was the plugin suite IRCAM Tools. In that release was the first incarnation of SPAT as a DAW plugin based on over 30 years of research with IRCAM’s Acoustic and Cognitive Spaces Team. After decades of development the next step was the full production environment for spatial audio - _Spat Revolution_ through the elegant simplicity of the graphic interface, _Spat Revolution_ represents a formidable achievement. It brings together the technical expertise from decades of academic research and development at IRCAM into an easy to use package that is flexible and powerful enough to meet all the demands of spatial audio production, from day to day surround sound post-production to the most challenging realtime installations. 
<br>
<br>
As you will discover _Spat Revolution_ can handle a virtually unlimited number of input and output audio streams and is prepared for all formats and 3D-audio workflows currently available or imaginable in the audio industry.

---

### Users and Applications

- post-production for film
- studio composition
- 360 video soundtracks
- 3D Audio for broadcast
- interactive sound art
- live production mixing
- scientific research and development
- sound design for film, music and theatre
- environmental sound

^ 
<br>
_Spat Revolution_ is aimed at all practitioners working in the medium of spatial audio and 3D sound production - old and new.  It is an expert system intended for professional use but its intuitive graphical interface invites a more diverse range of creators to engage in spatial sound production - if it is your first experience working with spatial sound technology, _Spat Revolution_ is a great way to start out directly with a professional quality level.
<br>
<br>
In the contexts of live concerts or sound installation, the composer or sound mixer can associate sound events with a room effect or a specific position in space. Virtual objects can be controlled on screen, or by a sequencer, a score-following system, or any other algorithmic approach. Spat can easily be linked to any remote control device (tracking systems, tablet, smartphone, joystick, gestural sensors, etc.) through OSC and RTTrPM interfacing protocols.
In the contexts of studio mixing and post-production, a virtual source can receive its audio from individual channels on a mixing desk with additional controllers easily set up to allow hands on control of the positions and characteristics of virtual sources and associated room effect. Spat Revolution can re-mix a multichannel mix from one format in a virtual room that could be rendered in a different output format, allowing a novel approach to up- and down-mixing.
<br>
<br>
In the context of Augmented and Virtual Reality, a spatialised auditory component is essential in creating the sensations of presence and immersion in interactive virtual reality applications. In such scenarios, the B-Format and binaural 3D capabilities of Spat is particularly well suited.
An important thing to keep in mind is the long heritage and technical expertise behind _Spat Revolution_. There are many critical factors to consider when multichannel audio is actually applied in the real world. But rest assured that the algorithms behind your spatial sound project are being implemented correctly at the stage of the authoring and rendering environment. It is good to know that _Spat Revolution_ is built with such a high level of technical expertise in such an intuitive
package.

---

### Spat Revolution, What is it? 

* An object based audio mixing software to create immersive audio content
<br>
* A suite compromised of the main audio application and 3 plugins for DAW / Show Control integration (various format)

---


### Spat Revolution Project

* From the SPAT plug-in to the SPAT Revolution project released in September 2017
<br>
* Revolutionary real-time immersive stand-alone software
<br>
* Complete, powerful and comprehensive toolbox for immersive audio sound-design and mixing
<br>
* Music/Post production, Composition, Live production, VR, Theatrical, installed sound and many more

---


### ![](include/favicon-32x32.png ':class=img-title')FLUX:: IRCAM Spat (2010)

![right 70%](include/ircam_spat-v3-full.jpg ':class=img-title')

[.hide-footer]

---

### ![](include/favicon-32x32.png ':class=img-title') Open Design Approach
[.hide-footer]

---

### Adapts to applications and workflows

* Simple integration to DAW for music creation (software I/O - local path).

* Ease of simultaneous rendering of deliverables (formats) of choice for production.

* Support ambisonic for format transcoding and as a spatialization technique.

* Offline sound designer tools with preview for larger speaker arrangements

* Support for any Core and ASIO I/O interfaces at all sampling rates

* OSC and Real Time tracking integration for Live 

---

### SPAT Live integration

* Local I/O or or Network connectivity (AES67/Ravenna, AVB and Dante) via ASIO/Core audio 

* Show controllers and playback such as QLab and Ovation 

* Real-time source or listener tracking (ex: Blacktrax RTTrPM)

* Open Sound Control (OSC) for various generic remote controllers 

* Spat Plug-in for Live Console Integration



---

## 2.1.2. Installation and Activation

![inline 40%](include/installationandactivation.png ':class=img-title')

---

## 2.1.2 Installation and Activation

**FOUR (4) STEPS to Install Spat Revolution;**
<br>

1. [Create an account](https://shop.flux.audio/en_US/login "") at Flux.audio
2. License code redeem
3. Software license activation 
4. Download and installation

---

### Create an account

![inline 65%](include/SpatRevolution_StoreLogin.png ':class=img-title')

[Create an account](https://shop.flux.audio/en_US/login "") 
If you have an received an activation code (such as from a dealer purchase)

---
### License Code

#### FLUX:: Immersive uses the iLok license management system to deliver software licenses to users.

![inline 60%](include/SpatRevolution_Redeem.png ':class=img-title')

Visit our [License Code Activation page](https://shop.flux.audio/en_US/account/licence_code_redeem ""). 

---

### iLok User Account

![inline 70%](include/SpatRevolution_Ilok.jpg ':class=img-title')


To activate licenses:


- An iLok user account is required.

- An iLok USB key is optional.

	(Cloud license currently not supported)


^ 
<br>
FLUX:: Immersive uses the iLok license management system to deliver software licenses to users. If you don’t have an iLok account yet, then please create a free iLok account at http://www.ilok.com and download the iLok license manager. A Flux Spat Revolution license come with two activations that need to be linked to your user account. Having two activations gives you the possibility of having a fixed license on one particular machine and a portable license on an iLok USB key if you own one, or a Main and Back up Spat Engine running on a live show.
	
---

### iLok License Manager

![inline 40%](include/SpatRevolution_Ilokpage.jpg ':class=img-title')

*If you have completed a purchase online or have redeemed your software license, it will already be delivered into your iLok account.*

^
<br>
For new iLok users, the first step is to download and install the iLok license manager available on the home page of the iLok website. When your user account is successfully activated and the iLok license manager correctly installed, you can start the software and log in to your iLok user account. Visit [iLok License Management Web page for software downloads](https://www.ilok.com/#!home). 

---

### Transferring license 

![inline 50%](include/SpatRevolution_IlokLicense.jpg ':class=img-title')

**Simply drag you license to the your Local Computer or on an iLok USB key. You are now set**


> If you require further information about iLok and managing licenses please refer to iLok.com website


^ 
<br>
Pressing on the _Sign In_ button will allow you to connect to your account. After Logging in, you are now ready to transfer any licenses to a computer or to any iLok USB key if you happen to have one. The process of transferring a license is as simple as dragging the license from the Available tab to your Local Computer *(or iLok key)* on the left side.

---

### FLUX:: Center 
![inline](include/SpatRevolution_FluxCenter_-017.png ':class=img-title')

^ 
<br>
Next step is to get the installers for the FLUX:: products you are licensed for. All the software and plugins from FLUX:: are available via our _FLUX:: Center_ software. This is a Mac or Windows application we have created to help keep your products up to date and to give you a clear overview of what you have installed. Firstly, please visit the download section of the FLUX:: Immersive website to get the installer for the FLUX:: Center application at [Download Page](https://www.flux.audio/download/). 
<br>
<br>
On this page you will find a Mac OS X, a Windows 32-bit and a Windows 64-bit version of the installer. After downloading and installing, you can open the FLUX:: Center application to begin the process of installing the Spat Revolution software.
<br>
<br>
!> An authentification is required at the launch of Flux Center. This is the login details of your Flux shop account.

---

### Center Login

![inline](include/Flux_Center_Login.png ':class=img-title')

^
<br>
A FLUX:: Shop account is now required to access the new FLUX:: Center. The Center now includes a _My Product Only_ view that filters only the products you currently have a license for.

---

### Center Preferences

![inline](include/SpatRevolution_FluxCenter_-021.jpg ':class=img-title')

^
<br>
When you open FLUX:: Center you will see a page that lists either _All Products_ or _My Products_ available for you to install. You will also find information about which version you have currently installed on your system and which new versions might be available for you to update as well. 
<br>
<br>
You can select versions to install - or uninstall if necessary - using the pull down menus. If you would like to access more installer options such as your preferred plug-in format, please click on the gear icon to the top right of the header area.

---

### Center Options
![right 65%](include/SpatRevolution_FluxCenter_-023.png ':class=img-title')
> *Spat Revolution Send/Room/Return plugins are available in VST-64bit, AU-64bit, AAX-64bit and AAX VENUE only.*


^ 
<br>
This preferences page will allow you to choose various installation options such as preferred plug-in formats for your system. Choosing your format and returning to the main page by pressing the OK button will show all your install options for software and plugins based on the desired formats chosen. When an option is enabled, the corresponding checkbox is pink. 
<br>
<br>
If you would like to be closer to the most current development cycles of the software, you can enable the Beta Versions option. This will give you access to the beta public software installers from the pull down menus on the main FLUX:: Center page. Beta versions are the new builds that are still under development but may contain useful bug fixes and new features.
<br>
<br>
If you find that a Beta Version is not stable enough for you, then you can always roll back to a stable release version at any time through the FLUX:: Center installer pull-down.

---

## 2.1.3. File and folder structure


* Resource files and folders
* File management
* Creating and saving sessions


---

### Spat Revolution files

Spat Revolution uses 3 different file types:

* .json
* .ioconfig
* .reverbPresets


^ 
<br>
<br>
*.json* are the main files of Spat Revolution: sessions are saved in this file type.
To save a session, click on the "Save session" button on the Setup page, or use the shortcut <code>Ctrl + S</code> on Windows, or <code>Cmd + S</code> on Mac, on any page of Spat Revolution.
<br>
<br>
User created custom speaker arrangement (s) can be exported or imported as *.ioconfig* files in the edit speaker config window. 
<br>
<br>
Reverb preset can be stored and exported as *.reverbPresets.* They can later be imported back into a session.

---

### Preferences and Ressource files

<code>Users/.../Document/FLUX SE</code>

<code>Users/.../Document/FLUX SE - IRCAM</code>

<code>Users/.../Document/Ircam</code>

★When backing up a system, make sure to copy all these folders to secure the  complete software configuration

^ 
<br>
The FLUX SE Folder contains a subfolder named *Config*  which has 3 file;
_.ioconfig_ contains your added speaker arrangements to Spat Revolution. _.presets_ contains your reverb presets. _.theme_ contains your theme (Dark or Light mode).
<br>
<br>
A subfolder named *Preferences* containing; _hrtf.json_ file which includes your HRTF files location. _users.json_ contains your saved software preferences. _Preferences.xml_ saves some paths. _UI.xml_ saves your user interface preferences. _Property Memory_ subfolder contains the memory slots saved by parameters. A subfolder named _Shell_ containing _history.txt_ an history of the terminal commands.
<br>
<br>
The FLUX SE - IRCAM Folder contains preferences and presets of the three Spat Revolution plug-ins.  
<br>
The Ircam Folder contains a subfolder called *sofa* which contains the sofa.catalog.xml file. The HRTF catalog.


---

### Paths for python scripts

<code>Users/.../Desktop</code>

<code>Users/.../Document/FLUX SE/Spat Revolution</code>

<br>
★An example of a script file is the ![customSpeakerArrangement](https://public.3.basecamp.com/p/rQStK3igPkaXisYS4Gs5sJ2g) that can be used as a method to add arrangements to Spat Revolution.

---

## 2.1.4.	Environment

[.hide-footer]

---

## 2.1.4. Environment
#### The Spat Revolution production environment is based around various graphical user interfaces.

* Environment Setup editor
* Speaker Config 
* Rooms (Virtual rooms) 
* Source and Parameters
* Reverberation Parameters

---

### Global and Status Bars
![inline](include/SpatRevolution_UserGuide_-070.jpg)
![inline](include/SpatRevolution_UserGuide_-072.jpg)


^ 
<br>
The Navigation bar appears at the top of all views. As well as links to different editor views and the Preferences, it also offers you the possibility to Mute and UnMute Rooms.
<br>
<br>
The Status and Help bar appears at the bottom of all views. It gives information about the status of audio connections, sample rate, block size and through latency.
<br>
<br>
Some online help also appears here when the mouse moves over elements of the SPAT graphical user interface. The _Provide feedback_ button sends a message directly to Flux support which automatically includes your system information for our support team.
<br>

---

### Environment Setup Editor

* Signal Routing, 
* Format Transcoding
* Panning Algorithms

![inline](https://media.githubusercontent.com/media/FLUX-SE/doc_images/main/SpatR/Setup/ModuleDragDrop.jpg)

^ 
<br>
This is where you will generally start a project by designing the signal flow graph that you will be working with. _Setup_ is also where you manage the loading and saving of projects to disk.
<br>
<br>
The _Environment Setup_ editor is a relatively simple modular environment. The signal flow starts from the inputs at the top of the graph and concludes with the outputs at the bottom. You add modules to rows using the small (+) icon to the left of the window.
<br>
<br>


---

### Setup Modules
The _Environment Setup_ editor is a relatively simple modular environment. The signal flow starts from the inputs at the top of the graph and concludes with the outputs at the bottom. You add modules to rows using the small (+) icon to the left of the window. Modules are;

* Inputs
* Input Transcoding
* Sources
* Room
* Sum
* Master Transcode
* Master
* Binaural Monitor
* Output 

---

### Setup Wizard

![inline](include/setupWizard.gif)

^ 
<br>
In our effort to make Spat Revolution easier to use, we created a small utility to help you set up new Spat sessions. This is used mainly when dealing with hardware I/O.
<br>
<br>
To open it, you can either :
<br>
The top part of the Setup Wizard, allows to create a new room (with associated options) or to select an existing room to patch new sources into. If a new room is created, we can choose its stream type and many options linked to it. We can also choose to associate a binaural monitoring block to it.  (virtualizing the room output) Lastly, for each new room created, a master block and an output block is also created.
<br>
<br>
The main part of the Wizard allows creating up to 8 different types of sources. It works like a table where each line can be used for a specific input stream type. To add or remove a line, simply click on the <code>+</code> or <code>-</code> sign on the left side of a line. You can also use the shortcut <code>Ctrl + Go Down</code> or <code>Ctrl + Go Up</code>.
<br>
<br>
When we have done creating out different sources, we have to way to validate the operation. We can  either click on <code>Ok</code>, all the sources, rooms and outputs will be created, with a straight routing, or, we can choose to click on <code>Ok +  matrix</code>. This last option will open the input and output matrix of our whole Spat Revolution session to allow us to quickly customize or validate our patch. 
<br>
<br>
Also, if you need to easily create a line in Spat matrix, simply hold CMD or Ctrl and click on the starting point of your line. 

---

#### Setup Wizard Confirmation

![inline](include/setupWizard2.gif)


---
### Inputs

![inline](include/SpatRevolution_UserGuide_-080.jpg)

> One Input module can represent any number of audio channels


^ 
<br>
It might be self-evident, but it's worth pointing out that Spat Revolution itself does not play audio files. It handles the spatialization and rendering of signal sources routed through it in realtime like some kind of vast spatial sound mixing console.
<br>
<br>
The second important distinction between inputs, is whether or not it is a **hardware** input receiving an audio stream from a hardware device or a virtual **send** receiving its audio stream from another program currently running on the same machine as SPAT. The latter is done via a Spat Revolution _SEND_ plug-in - but before we go into Spat's powerful software signal routing integration, let's focus on the different input formats as these will remain consistent whether the input stream is coming from hardware or from a _SEND_ plug-in.

---

#### Input naming

![inline](include/SpatRevolution_InputNames.png)

* Select an input in the setup page and rename it in the inspector in the right side.
* Select multiple inputs blocks and to choose the option "Edit Inputs Names" 

^ 
<br>
There are two ways to rename an input. The first solution is to simply select an input in the setup page and to rename it in the inspector in the right side of the Spat Revolution window.
<br>
<br>
If multiple input need to be renamed, the previous method can be tedious. The solution is to select multiple inputs blocs and to choose the option "Edit Inputs Names" in the inspector, or use the shortcut <code>Alt + N </code>. A new window will open with a list of all the selected inputs, ready to be renamed. To quickly navigate through the input names we can use either the "enter" or "tab" key.

---


#### Mono Input

A one channel audio stream is always treated as a Mono signal. It will appear in a
_Virtual Room_ as one positionable virtual source with its own directivity and parameters. In many ways, Mono signals are the most straight forward format to work with
in a spatial composition. This is because a one channel signal discretely contains all
its acoustic and spectral properties without inter-channel dependencies, such as
those found in a wide stereo image for example. In practice, such point sources are
easier to localise and balance spatially with others.

> ★ Mono sources are simple to work with when balancing a spatial mix

---

#### Two Channel

- **Channel Based**
    Treated as Normal stereo
- **Mid-Side (MS)**
    Treated as Mid Side encoded stereo
- **Binaural / Transaural**
    Treated as encoded 3D stereo

^ 
<br>
A two channel audio stream will appear in the _Virtual Room_ as two mono sources linked together as a group. A two channel audio input will already open a few more choices for disambiguating the configuration. Spat needs to know what format the two channels are in, so it knows how to correctly handle the audio stream later in the signal flow.



    
---

#### Four Channel Input

##### The next significant channel count that needs disambiguation from the user, is a four channel stream.

![right 100%](include/SpatRevolution_UserGuide_-082.jpg)

^
<br>
A four channel stream could contain the format of a four speaker Channel Based formats (QUAD, 4.0, LCRS) but could also contain different formats of interleaved four-channels Ambisonic audio (A-Format, B-Format). We will cover more about A-Format and B-Format in the [Ambisonics Section]() section of this user guide. The important thing to remember here is that confusing Ambisonic audio and Channel Based audio is a significant mistake, even though you might hear something 'wide sounding'.

!> Do not confuse multi-channel based audio formats with multi-channel Ambisonic audio formats. 
They may have the same channel counts but are completely different!

---

#### Multi-Channel Based Input

> ★ Try to stick to industry standard channel naming conventions throughout a cinematic surround sound project


^
<br>
Any input module configured to represent a stream of multi-channels audio can be configured as a Speaker Arrangement format which would require that amount of channels, as a minimum.
<br>
<br>
For example, _DTU 7.1_ needs 8 channels, and _DTU 5.1_ needs 6. _Auro3D 13.1_ needs 14 channels. Unfortunately things can get complicated in practice, as there are a few variations of standardized speaker layouts which have the same number of channels and seem very similar - but need disambiguation. This is important to get right, and will depend a lot on the context of your
project and on changing standards in the audio industry. For example, at least four different 7.1 routing standards are to be found 'in the wild' and its important to know which one you are actually dealing with. Often, for example, the so-called 'Low Frequency Effects' channel in cinema surround formats, is not always on the same channel.
<br>
<br>
L | C | R
---|---|---
sL | | sR
surround Left | | surround Right
  | LFE |
  | Low Frequency Effects |
sbL | | sbR
surround back Left | | surround back Right.
<br>
<br>
Some common Speaker Channel naming abbreviations. Please refer to Appendix C for special information about handling LFE and Mono. Sub Woofer routing in Channel Based applications.

---

#### Multi-Channel Ambisonic Inputs
- 1st Order 2D -> 3 Channels
- 2nd Order 2D -> 5 Channels
- 3rd Order 2D -> 7 Channels
- 4th Order 2D -> 9 Channels
- 5th Order 2D -> 11 Channels
- 6th Order 2D -> 13 Channels
- 7th Order 2D -> 15 Channels
<br>
<br>
- 1st Order 3D -> 4 Channels
- 2nd Order 3D -> 9 Channels
- 3rd Order 3D -> 16 Channels
- 4th Order 3D -> 25 Channels
- 5th Order 3D -> 36 Channels
- 6th Order 3D -> 49 Channels
- 7th Order 3D -> 64 Channels

^
<br>
As we have mentioned a few times already, High Order Ambisonics is a technology that encodes sound sources along with full sphere positional information, as complex interleaved audio files that need decoding before they can be listened to on. The lowest order of 3D Ambisonics requires 4 channels, conventionally named as;
- **W** (mono sum)
- **X** ( X axis information)
- **Y** ( Y axis information)
- **Z** (Elevation information)
<br>
<br>
This is the conventional _B-Format_ also known as _First Order Ambisonics_. Some Ambisonic microphones record into a very similar four-channel format called A-Format, which ideally needs transcoding into B-Format. You can use the Input Transcoder Module to do that (see next section). There are a number of options that some Ambisonic encoders set differently to others, and these are sometimes concerned with the actual order of the WXYZ - for example a format called **Ambix** has a different order of channels that carry the spherical components, compared to
<br>
<br>
- for example a format called **Ambix** has a different order of channels that carry the spherical components, compared to **FuMa**. It is possible to configure channel sorting and normalisation options in the Input and Input Transcoder modules, and at any point where Ambisonic streams are decoded to a channel based stream. Please contact Flux:: support if you need expert guidance in the area of Ambisonic decoding options, as the topic is very large, and is beyond the scope of this guide.
<br>
<br>
High Order Ambisonics (HOA) needs more channels to contain the complex interleaved Ambisonic domain information. High Orders encode and decode into sharper and more accurate spatial information as the Order gets higher - but the number of channels needed to hold all the 'spherical harmonics' along with the serious computation involved, becomes very complicated very quickly.
<br>
<br>
★ Spat Revolution makes it easy to work with High Order Ambisonics. Just dial up the Higher Orders using the pulldown menu of an Ambisonic Input module, Transcoder or Ambisonic Room. The output stream will then expand its channels internally to accommodate the higher channel count needed. 3D full sphere HOA channel counts are defined by the function (n+1)^2 (where n = Ambisonic Order)
<br>
<br>
_B-Format_ can also be encoded without elevation - this is called 2D horizontal and is quite suitable for decoding to configurations that do not have speakers on elevated planes. The 2 dimensional Ambisonics data is encoded in multichannel files with a channel count defined by the function 2n+1.


---

### Input Transcoder

![left 35%](include/SpatRevolution_UserGuide_-084.jpg)

^
<br>
Spat Revolution can handle many different formats of multichannel audio throughout the signal flow, as we have been pointing out. As we approach the actual virtualization of inputs into object based audio sources in the Spat _Virtual Rooms_ it may be necessary to change from the original input format to another. You use the Input Transcoder module and its parameters to do this.
<br>
<br>
Transcoder modules may modify the channel count of the stream passing through it, depending on the format transfer being requested. For example, transcoding from Ambisonic B-Format into a Channel Based 3D Cube involves a four channel Ambisonics stream getting transcoded into an eight channel stream grouped and treated as a specific speaker configuration.

---

### Transcoding Matrix


![inline](include/SpatRevolution_UserGuide_-086.jpg)

^
<br> 
In the case where an incoming Channel Based stream needs transcoding into an outgoing Channel Based stream which has less channels, the IO Matrix is used to re-map the output format by dropping some of the input channels. Similarly, if the transcode results in a format with more channels than the input format, the IO Matrix is used to remap inputs to outputs. 
<br>
<br>
This is not strictly _Transcoding_ or _decoding_ but is a useful tool to have in certain format changing scenarios. To properly up mix or down mix, it is advisable to use a room to take the virtual source of one format, and output with the desired end format.
<br>
<br>


---

### When to Transcode Inputs?

![inline](include/SpatRevolution_UserGuide_-088.jpg)


^
<br> 
The main reason you will need to transcode inputs is when you are mixing and spatialising inputs in a Spat _Virtual Room_. This is because the _Virtual Room_ module requires incoming sources to be in a Channel Based format. Internally, the Room may well be panning in Channel based, Ambisonics or binaural format, but it always needs Channel Based streams as inputs. More about this in the _Virtual Room_ section. Format transcoding may not always need re-spatialising in a Room. 
<br> 
<br> 
There are some contexts where you will not use a Virtual Room in the signal flow, Here is an example of decoding an Ambisonic signal using an Input Transcoder module. This could also be done in the Master Transcoder section of the graph. As mentioned in 'Introduction to Ambisonic' a decoding stage is absolutely necessary to render Ambisonic encoded audio to speakers. It can be done like this without the need of a room.

---

### Rooms

---

### Master Section

![inline](include/SpatRevolution_UserGuide_-124.jpg)


^
<br>
The **Sum** row of modules is used to mix the output of two or more Rooms of the same output configuration and in some contexts, to sum inputs directly without the use of Room.
<br>
<br>
The **Sum** module can handle different input configurations.  It will Sum channels based on their channel names, so a correct naming convention is important. Summing a 5.1 and 7.1 room together will output a 7.1 where they're common L, C, R, Left and Right Surround rear channels will have content summed from both rooms the but Left and Right Back surround will be only from the 7.1 room.
<br>
<br>
Summing can also be done directly in Master and Output Modules, but summing into sum will save resources the same sum is performed in different blocks. The **Master Transcoder** row of modules offers an opportunity to consolidate the various formats you might have been mixing into one (or more) formats for final output routing by the **Output** modules. 
<br>
<br>
The same options and routing are available as in the _Input Transcoder_ modules. Finally, the two bottom rows in the _Environment Setup_ graph are the output modules for the entire project.
The [**Binaural Monitoring**]() row provides a way to decode the whole scene to headphones only in binaural 3D.

---

### Output

![inline](include/SpatRevolution_UserGuide_-126.jpg)

^
<br> 
The main thing to note at the output stage is that you can have any number of output routes. 
Like the [Inputs](), they may be either direct hardware routes, which returns audio streams (via Matrix routing) to the physical outputs of an audio interface connected to your Spat Revolution workstation. 
<br> 
<br> 
The Hardware Output workflow is the most direct way to render in realtime to an actual loudspeaker system (or headphones).
<br> 
<br> 
Outputs may also be linked to Spat Revolution RETURN plug-ins, which returns audio streams internally on the same workstation to a valid Spat RETURN plug hosted in your DAW. 
The software RETURN workflow offers an easy way to render the spatial scene to disk, as _Ambisonic encoded_ , _Binaural encoded_ or _Sound system encoded_ multichannel audio.
<br> 
<br> 
> Create multiple output routes to capture Ambisonic recordings at the same time as sound system specific rendering.

---


### Modules connections

![inline](include/SpatRevolution_UserGuide_-074.jpg)

> Select multiple modules using drag/lasso selection before an Action
> Modules can be connected to multiple destinations 
> Modules can received from more than one module and offer input summing.


^ 
<br>
Connect or disconnect modules by using _command+click_ to select some followed by any of the Actions available in the options panel on the right of the window. Various keyboard shortcuts are also available for each Action. As you connect modules and build up a signal graph, you will see some 'wires' appear which connect modules together. 
<br>
<br>
In Spat Revolution these 'wires' represent connections in the signal graph diagram, you do not directly interact with them. It is not a 'patching' type of interface.
<br>
<br>
There is no UNDO/REDO paradigm in the signal graph editor at this point. Instead it is advisable to use **Connect/Disconnect Selected** actions to re-structure the signal graph. Try to avoid deleting modules until you are certain that is the correct action.
<br>
<br>
It is possible to connect some modules, such as Input or Source, to multiple destinations, as a way of making doubles in a single or doubling a single source into different virtual rooms.



---

### Rooms (Virtual Scenes)

* Dynamic control
* Spatial positioning
* Scene Visualisation
* Mixing

^ 
<br>
★ Virtual scenes are rendered as graphics on a monitor screen as sounds in a physical space and as stems to disk.
<br>
<br>
★ Spat Revolution gives you an unprecedented level of control over the position and characteristics of virtual sound sources placed in virtual spaces. This is the main function of the Virtual Rooms editor where you can adjust and visualize the position and acoustic characteristics of virtual sound sources and compose virtual scenes with them on screen.

---

### Nebula Spatial Spectrogram

![left 40%](include/SpatRevolution_UserGuide_-102.jpg)

^ 
<br>
_Nebula_ is a technology adapted from our flagship **FLUX:: Analyzer System** a suite of highly regarded professional mastering and mixing visualization tools. **Nebula** in Spat Revolution provides a unique representation of the sound field in terms of spectral content and localization rendered directly inside the 3D speaker simulation and virtual room display. It combines the functionality of a spectrum analyzer and a vector scope in a novel real-time display. It is a useful tool to get a realtime overview of your spatial mix in terms of spectral-spatial diffusion, and can give quite accurate representations of 'where' and 'how' sounds will manifest over a real world sound system. A lot of work has gone into optimizing the real-time rendering of the display, not solely for aesthetic reasons, but because we wanted the display to react instantly to all the details in the incoming multichannel audio. The idea is literally for you to be able to see what the listener will hear and feel.
<br>
<br>
**How does it work?**
The overall principles behind _Nebula_ are quite straightforward. At any given time, and for every frequency, the engine computes the position of a frequency in space (2D in stereo and 3D for multi channel surround). This position is taken as the center of gravity of the various channels, weighted by the relative amplitude of the signal in their corresponding channel. A colour-intensity mapped projection is computed for the multi-speaker plane, giving a spectrum-space frame constrained to the surround sound field radius or sphere. Past analysis frames are progressively “forgotten”, using blur and dimming, in order to make place for new information, which gives the graphic display increased legibility and its characteristic 'nebulous' quality.

---

### Speaker Editor
![inline 30%](include/SpatRevolution_UserGuide_-033.jpg)

On channel based stream, a Speaker Editor is available to edit the speaker arrangement to match a model of the sound diffusion system and offer the managements possibilities.

> Pre-defined arrangements cant't be edited but can be duplicated and modified


---

### VU Meters

![right 40%](include/SpatRevolution_UserGuide_-078.jpg ':size=250')

[.hide-footer]

^ 
<br>
Throughout Spat Revolution's different editors, you will see a complete set of accurate decibel meters giving you a visual display of all channels activity in an audio stream, whether Ambisonics or Channel Based. 
<br>
<br> 
They are very useful to see when clipping might be occurring in any of the channels, and to debug signal flow routing in general.
<br>
<br> 
Also, notice how the 'wire' that graphically connects Modules in the Set Up signal graph does not visually change even though it is handling a load of channels.
<br>
<br> 

---

### Matrix

As routing and patching high density channel counts can get complicated, the SPAT routing matrix is there to help. You will find it at many points throughout the **Environment Setup** inspector of modules. This is there to facilitate hardware input and output routing as well as remapping within modules) 


![inline](include/SpatRevolution_UserGuide_-031.png)

---

### Preset Memories

Each parameter has the possibility to store useful preset settings of your own choosing. Right click on a parameter dial, and a contextual menu will pop up. From there you can store the current setting to a Memory Slot, or Recall a setting from a previously save memory slot.

![inline](include/SpatRevolution_UserGuide_-148.jpg)

<div style="display:none">
### Automation state

Each parameter can be set in four different automation states: isolate, play, record, auto-write. When set to isolate, the parameter cannot be automized. When set to play, the parameter is listening for automation. When set to write, the parameters will always send write automation. By default, all the parameters are set to auto-write: the auto-write is comparable to a latch mode.

![](include/spatAutomationState.jpg)

</div>

---

### Reset to defaults

A double click on any dial will reset it to a Spat default setting. The default setting of a parameter is indicated around a dial as a larger tick than the other tick marks. Additionally a range is graphically indicated between the default setting and the current setting of a variable parameter.

![inline](include/SpatRevolution_UserGuide_-162.jpg)

> ★ _Use the defaults as points of reference in your spatial sound design_

---

### Source Transformation
#### To open the transform menu, right click on a source in the source panel and choose "Transform".

<code>CMD/CTRL + SHIFT + T</code>

![left 130%](include/SpatRevolution_SourceTransform.png)


^ 
<br>
As with the custom speaker arrangement editor, we can apply some transformation to one or multiple sources. This feature is especially handy if you wish to quickly set sources on a circle, or to put a selection of sources at the distance for exemples.
<br>
<br>
Check the section about [Speaker Arrangement](Spatialisation_technology_Speaker_Arrangement.md) if you want more detail about the different transforms.
Sources transformations also include an integration time which allow to create smooth transition between the current and the new sources position.


---

## 2.1.5.	Application preferences

* Configuring  hardware I/O (Core and ASIO)
* Working with software or hardware I/O
* Engine Core Configuration
* Integration ports (OSC, RTTrPM, Midi)
* User Interface options


---

## 2.1.5. Application Preferences

![inline](include/SpatRevolution_UserGuide_Preferences.png)

---

### Global

![inline](include/SpatRevolution_UserGuide_Pref_Global.png)

^ 
<br>
Inside this panel you will find various option on the general behaviour of Spat Revolution. The first one is "Allow sending error data". When set to on, error data that may occur when using Spat Revolution on your system will be anonymously sent to Flux:: Immersive.
It may sometime fasten your workflow to automatically recall the last opened session. You can do this by activating the option "Re-open last session on startup".
<br>
<br>
Depending on where you live in the world, you may prefer use the metric system or the imperial system. When "Use Metric System" is on, distance will be expressed using the metric system.
The temperature has to be set accordingly to the ambiant temperature of your room. It affect how delays are calculated inside the Spat Engine.
<br>
<br>
Depending on the performance of you hardware, you may want to be adjusting frame rates. The edit frame rate set-up the frequency refresh of the UI. The engine frame rate is how often the engine update acquire new informations. Finally you can also set-up the refresh rate of the meters.

---

### Hardware IO

![inline](include/SpatRevolution_UserGuide_Pref_Hardware.png)

^ 
<br>
This panel allows to select an audio device when needed to bring hardware inputs. There is also options for the sample rate and the buffer. Remember that they should always match the settings of the selected interface. Also, if you wish to use Spat Revolution with plug-ins only, choose no audio device.
<div style="display:none">
external samplingRate - Are we removing this?
</div>

---

### User Interface
#### Options 
![left 100%](include/SpatRevolution_UserGuide_Pref_UI.png)

^ 
<br>
This panel gives some user interface options. If your computer have a dedicated graphic card, you may want to leave the anti aliasing on. If not, disabling it will release some of the graphic processing for a performance boost.
<br>
<br>
The "Setup Wire" option will change how the wire in the setup page are drawn. By default, it is set to spline. If this option is deactivate, the wire in the setup page will be straight.
In Spat Revolution two theme are available. Dark or Light mode. Light mode is also known as positive contrast polarity  and refers to dark-font text on light background. 
<br>
<br>
A list of all the shortcuts of Spat Revolution is available as a popup menu when pressing the "Shortcuts" button.

---

### OSC Main
![right 100%](include/SpatRevolution_Enable_OSC.png)

* Enabling and monitoring OSC data

* The "Enable Commands Log"

* "Export Parameters"

^ 
<br>
OSC Main allows you to enable OSC (Open Sound Control) globally. Enable commands log will display the received and emitted OSC messages in the log windows to confirm you are receiving data. <code>Shift + F7 </code> will open the log window.
<br>
<br>
The "Export Parameters" allow to create a text file with all the OSC dictionary of Spat Revolution.

---

### OSC Connections
#### Connections Matrix
![left 100%](include/SpatRevolution_UserGuide_-195.png)
 
^ 
<br>
See OSC interaction and integration section.

---

### HRTF
#### Default HRTF and Management 
![right 100%](include/SpatRevolution_UserGuide_Pref_HRTF.png)


^ 
<br>
In this panel, you can choose your default HRTF (Kemar by default). The and "Manage HRTFs" allows you to include more HRTF from the database and import personalized HRTF.  See Binaural methods section for more information 

---

### Room
#### Apply a global gain trim to all rooms. By default it is set to 0dB.

![left 100%](include/SpatRevolution_UserGuide_Pref_Room.png)


<div style="display:none">
### Engine

The "Number Of Core" let you declare the number of CPU core of your computer. It is automatically set to the right number.
(need more info here)

</div>

---

### Blacktrax RTTrPM
#### Management of the integration of Blacktrax tracking system

![right 100%](include/SpatRevolution_UserGuide_Pref_Blacktrax.png)


^ 
<br>
In this panel, you can choose enable the integration of Blacktrax tracking system, choose the number of maximum Blacktrax beacon you are listening to (Up to 64), choose a specific network interface if needed and change communication port number when required. See Appendix Real Time Tracking using RTTrPM. 

---

# 2.2. Immersive Workflow Introduction                                                         

[.hide-footer]

---

# 2.2. Immersive workflow introduction

* Polar vs Cartesian coordinate systems
* Audio integration: Hardware & virtual software inputs
* Spat remote: OSC & Snapshots
* Typical set-up:
  * One computer workflow
  * Two computer workflow
  * Basic live set-up
  * Advanced live set

---

## 2.2.1. Immersive system Integration

[.hide-footer]

---

### Spat Revolution: an open system

[.hide-footer]

<div style="display:none">
Comment: Need a picture
</div>

---

### Polar or cartesian coordinate systems?

* Both polar and cartesian method simultaneously
* Cartesian (xyz) or polar (aed) coordinate 
* X (Left to Right), Y (Front to Rear), Z (Height)
* A (+/- 180 ° azimuth), E (+/- 90 ° elevation), D (distance length)

> *★Most systems will support only one system. Spat supports both!.*	

^ 
<br>
Dealing with source and object positions automatically means that coordinates will be required. Spat Revolution supports both polar and cartesian method simultaneously. 
This is actually is simple question of geometry: we can either define the position of a source with cartesian coordinate (xyz) or polar coordinate (aed). 
<br>
<br>
The later refers to Azimuth (degree), Elevation (degree) and Distance (in length). 
These coordinates are in reference to the center of the field, sometime called the listener reference when diffusion systems are surrounding the center.
<br>
<br>
Most of immersive audio engine only support one of the coordinate system. While it may seems sufficient at first, in practice, some movement and trajectory are simpler to express in one system over an other.

---

### Audio integration: from studio to large live production

* Stand-Alone and using generic hardware.
* Single computer workflow for easy portable studio production.
* Can be deployed on a network of computers with redundancy.


> *★ From creation to delivery and diffusion!.*

^ 
<br>
Spat Revolution was designed to handle almost any scenario of audio production, from a one computer casual studio to a larger live production with multiple computer and redundancy. This flexibility is achieved thanks its stand-alone operation.
<br>
<br>
At its heart, Spat understand two type of audio input: "hardware inputs" and "software virtual inputs". A "hardware input" is an input coming from an audio interface. It can be from a simple all-in-one audio interface with physical input or from a network interface like DANTE or AVB. At the base is the support for any Core audio (MAC) and ASIO (Windows) devices.
<br>
<br>
The "software virtual inputs" is where Spat Revolution is used on a single computer in a workflow with a digital audio workstation (DAW) providing the audio and automation. This is achieved with plug-ins.
<br>
<br>
Spat Revolution suite comes with a bundle of three plug-ins. Two are called "Spat Revolution Send" & "Spat Revolution Return". These two plug-ins act as virtual cable to connect a third-party DAW with Spat Revolution. With this support we can virtually interface any DAW with Spat Revolution application engine.

---

### Control integration: plug-ins, OSC and third-party

* Automation from DAW with local audio or via OSC.
* Multiple OSC connections possible to third party.
* Snapshot systems to create, recall and manage scenes.

>*★ Multiple integration options!.*

^ 
<br>
Because Spat Revolution adopts a very open approach, it provides many ways to access its controls, either for automation or live remote.  The Spat Send and Return plug-ins can send automation information together with the audio stream (Local Audio Path - LAP). 
<br>
<br>
That said, on larger systems with multiple computers and interfaces, the three plug-ins will use Open Sound Control protocol (OSC) over the network to send and receive control informations.
OSC is at the very heart of Spat operability. Any controller supporting OSC can be configured to work with Spat Revolution. You can actually use Spat Revolution to actually remote another instance of Spat Revolution in a kind of remote-server fashion.
<br>
<br>
At last but not least, Spat Revolution includes a snapshot system to manage internal automation of scenes. These scenes can be created, updated and easily recalled. They even can be remotely use by using OSC commands as well

---

### Typical systems

!> Need a nice picture here

[.hide-footer]


---

### Single computer workflow

![inline](include/oneComputerSetup.png)


<div style="display:none">
Comment: temporary diagram
</div>

> *★ Audio and Automation using plug-ins in Local Audio Path mode!*

---
[.background-color: #333]

![80%](include/SpatRevolution_UserGuide_OneComputer_ProsCons.png)

[.hide-footer]

---
### Dual computer workflow

![inline](include/twoComputerSetup.png)


<div style="display:none">
Comment: temporary diagram
</div>

* _MADI or AoIP solution to send audio between the two computer_
* _DAW Automation via Spat Revolution plug-ins in OSC mode_
* _Control via DAW remote or with third party OSC remote (ex: Lemur)_

---

[.background-color: #333]
![80%](include/SpatRevolution_UserGuide_DualComputer_ProsCons.png)

[.hide-footer]

---

### Basic live system


![inline](include/basicLiveSetup.png)

<div style="display:none">
Comment: temporary diagram
</div>

---
[.background-color: #333]

![80%](include/SpatRevolution_UserGuide_BasicLive_ProsCons.png)

[.hide-footer]

---
### Advanced live production systems

![inline](include/completeLiveSetup.png)


<div style="display:none">
Comment: temporary diagram
</div>

---
[.background-color: #333]

![80%](include/SpatRevolution_UserGuide_AdvancedLive_ProsCons.png)

[.hide-footer]

---

# 2.3. Implementation of spatialization techniques                                                        

[.hide-footer]

---

# 2.3. Implementation of Spatialization Techniques.


* 2.3.1. Speaker Arrangement and Calibration
* 2.3.2. Conventional 2D and 3D panning 
* 2.3.3. Binaural methods in Spat Revolution
* 2.3.4. WFS - Wave Field Synthesis in Spat Revolution
* 2.3.5. Higher Order Ambisonic in Spat Revolution (HOA) 

---

## 2.3.1. Speaker Arrangements and Calibration

[.hide-footer]

---

### Rendering To Speakers


* Virtual scene is transposed to a speaker system.
* Speaker arrangements to model the diffusion system.
* Panning or Synthesis method.
* Arrangements used for source, room and transcode.
<br>
> *★Pay attention to arrangements and channel routing, they are the key !.*

	
^ 
<br>
In order for the virtual scene to translate correctly as an immersive sound experience in a speaker format, SPAT needs to have an accurate model of a _multi-channel speaker arrangement_ which will be used to map the multi channel information to the destination speakers and render the sound field correctly in a real space. 
<br>
<br>
To this end, you will find a large library of standard and specialized speaker arrangements already built into SPAT which can be used in various places throughout the **Environment Setup**.
<br>
<br>
Speaker configurations can be used to fit the format of a virtual room to match the actual speaker system being used to diffuse the mix in a real room. Channel based speaker configurations can also be used to transcode the format of a virtual source into a virtual room. More about this later.
<br>
<br>
The golden rule when working with multichannel based audio is that you must be sure to choose _exactly_ the right formats, speaker arrangements and channel routing throughout, otherwise the virtual space will not map correctly into a physical space.



---

### Custom Arrangements

![inline](include/SpatRevolution_SpeakerConfig_1.png)

> *★The speaker configuration window showing a pre-defined 13.1 Auro 3D speaker arrangement.*

---

The **Speaker Config** editor offers the ability to prepare the model of the sound diffusion system you are actually using. 

![inline](include/SpatRevolution_UserGuide_-035.jpg)


^
<br>
When you find yourself working on a custom multi-channel speaker arrangement, the **Speaker Config** editor is where a model of the sound diffusion system can be defined and stored into the list of speaker arrangements. 
<br>
<br>
Open the **Speaker Configuration** editor by clicking on the <code>Edit</code> button of a Channel-Based room, by the _Speaker Arrangement_ pull down menu. Pre-configured arrangements cannot be deleted but can be **duplicated**  (a copy will be generated for editing) or a **New** config can be created.
<br>
<br>
Managing the **Speaker Config**uration includes the ability to **delete**, **rename**,  **import** configuration(s) from a file, or **export** configuration(s) to a file. Note that Spat Revolution’s pre-defined speaker arrangements can’t be deleted or renamed, but duplicating them (making a copy) will allow you to edit the arrangement thus starting from an existing configuration. 
<br>
<br>
Once editing a speaker configuration, you can either **+ Add, - Del, Move Up or Move Down** speakers in the list. Note that the total number of channels in your arrangement is denoted above the list. Your speaker system contains a Low Frequency LFE channel where you want the ability to send audio to it like on an aux system? Simply adding a channel (or channels), called LFE, will do the magic for you  directly. This particular channel won’t be fed from the virtual room panning, but by the LFE Send on each of the sources that will be available on rooms containing an LFE. 

---


## Speaker Config Window
### ★Editing a speaker configuration showing a copy of a 13.1 Auro 3D speaker arrangement.*

![right 120%](include/SpatRevolution_SpeakerConfig_3.png)

[.hide-footer]

---

![inline](include/SpatRevolution_UserGuide_-037.jpg)


> *★Computing and using the Normalize function.*


^ 
<br>
 Managing the **Speaker Configuration** includes the ability to <code>Delete</code>, <code>rename</code>,  <code>import</code> configuration(s) from a file, or <code>export</code> configuration(s) to a file. Note that Spat Revolution’s pre-defined speaker arrangements can’t be deleted or renamed, but duplicating them (making a copy) will allow you to edit the arrangement thus starting from an existing configuration. 
<br>
<br>
Once editing a speaker configuration, you can either <code>+ Add</code>, <code>- Del</code>, <code>Move Up</code> or <code>Move Down</code> speakers in the list. Note that the total number of channels in your arrangement is denoted above the list. 
<br>
<br>
Your speaker system contains a Low Frequency LFE channel where you want the ability to send audio to it like on an aux system? Simply adding a channel (or channels), called LFE, will do the magic for you here directly. This particular channel won’t be fed from the virtual room panning, but by the LFE Send on each of the sources that will be available on rooms containing an LFE. 
<br>
<br>
!> Importantly, **_LABEL_** speakers to unique names as the naming convention is used for summing audio streams

---

## Speaker Position

![inline](include/SpatRevolution_UserGuide_-039.jpg)

> *★Positioning Speakers with XYZ or AES coordinates.*

^
<br>
Position information of the loudspeaker can be entered as X, Y, Z in meters or with Azimuth degrees, Elevation degrees, and Distance in meters. These position have an origin of (0,0,0), the Listener Positions, the center of reference. Delay and Gain can be used to manually align the speaker location to a virtual "aligned" speaker, essentially creating a virtual speaker.
<br>
<br>
Spat Revolution can accept real world absolute measurements which you have entered manually, and this speaker arrangement can be used in all Channel Based contexts, such as an input array of microphone, simulating the exact physical speakers in a virtual room, virtualizing the speaker sources in binaural or transcoding into channel-based system from an Ambisonic stream.
<br>
<br>
> A detailed tutorial on advanced scripting of Custom Speaker Configurations using the Python language is available as in some cases, creating speaker setups in an editor is not the most efficient way, primarily when such information is available as a list and was exported by an acoustic and design simulation software like those used with loudspeaker companies. This can be quite practical for some larger more complex setups. See scripting section.

---

## Speaker Config Import

![inline)](include/impSpkArr_image.png)

^
<br>
For systems that are regularly changing such as in live production, setting up the speaker configuration in the simulation software and then  repeating it in the immersive software is not the most fun part!
<br>
<br>
To ease this part of the setup, you can now import from software of Nexo (NS-1), Adamson (Blueprint), d&b (ArrayCalc), CODA Audio (System Optimiser) and the standard EASE software.
<br>
<br>
This import is integrated into the "Speaker Config" editor where you can find the Import from button.
<br>
<br>
To begin is the FLUX IOConfig. This is the FLUX:: speaker arrangements file format. This can be a great tool to export and save your FLUX:: arrangements or to import an arrangement into another session / computer system.
<br>
<br>
In Spat Revolution, it is important to understand that speaker arrangements **DO**  follow the session file. So if you are opening a .JSON with an arrangement new to you system, Spat Revolution will create that arrangement and it will then be part of the user created arrangements always available. 
<br>
<br>
You care to know where these arrangements are stored? **Document/FLUX SE/Spat Revolution/Config** is where your master IOCONFIG file is located. (It includes all the  manually created or automatically created by session opening). Note that the repertory **Document/FLUX SE/Spat Revolution** is now the folder that contains all of your Spat preferences. A troubleshooting trick is to thrash this folder if data as become  corrupted. (Spat not opening for example). So yes, exporting your  arrangements or backing up Document/FLUX SE/Spat Revolution is never a  bad practice!
<br>
<br>
How to import a speaker configuration from:
**Nexo NS-1 :**
In NS-1, to export all the speakers : Go to the <code>Speaker Positions Windows</code>,  <code>Speakers/Speakers Position</code> or <code>Ctrl + P</code>. Select all the Speakers, and click on <code>Export, File...</code>. This will export a .txt file, readable by Spat Revolution.
<br>
<br>
**Adamson BluePrint:**
In BluePrint, to export all the cabinets: Go to the Cabinet tab. In the  line <code>Cabinet Group</code>, click on the 4th button, <code>Export All Cabinets</code>. This will export an .arys file readable by Spat Revolution.
![image(1)](include/impSpkArr_image(1).png)
<br>
<br>
**d&b ArrayCal:**
In ArrayCal, export all the sources with "Files/Export/EASE/Coordinates of all sources". This will export a .xld file readable by Spat Revolution.
![image(2)](include/impSpkArr_image(2).png)
<br>
<br>
**Excel**
![image(2)](include/speaker_import_excel_example.png)


---
## Speaker Transformations

To modify a speaker arrangement with a predefined action, you can use the "transform" menu. To access it, click on the "Transform" button. A pop-up window will appear.

It is know possible to apply specific transform function to the speakers present in the arrangement. It can be done with the "transform" menu. To access it, click on the "Transform" button. A pop-up window will appear.

![Inline](include/SpatRevolution_TransformSpeakers.png)

^
<br>

**Normalize Distance**; The further speaker will be place at the given distance. All the other speakers will be placed at the relative distance from it.
<br>
<br>
**Set Elevation**: The first ring of speakers will be placed at the given elevation.
<br>
<br>
**Offset Distance**; This transform applies an offset to the distance parameter of all speaker. It preserves relative position of speakers.
<br>
<br>
**Offset Position XYZ;** Same as above but with XYZ parameters.
<br>
<br>
**Scale Distance**; This transform allows to scale all the speakers inside a certain range of distance. It preserves relative position of speakers.
<br>
<br>
**Scale XYZ**; Same as above but with XYZ parameter.
<br>
<br>
**Rotation Azimuth**; With this transform, we can apply a rotation to our speaker array.
<br>
<br>
**Mirror**; As its name imply, this transform create a mirror of the speaker arrangement regarding of a certain axis.
<br>
<br>
**Linear uniform distribution along the selected axis**; This transform puts all the speakers on the same axis, with an even space between them.
<br>
<br>
**Circle**; This transform places all the speaker on the same circle, with an even space between them.
<br>
<br>
**Sinus**; This transform creates a sinus shape with the speakers.
<br>
<br>
> The **Normalize** can be used to rapidly scale down the speaker arrangement to have the furthest away speaker distance set for example to 2 Meters only. All predefined arrangements have this normalization. This 2 Meters is as well the default source distance which brings consistency from room to room., This helps as well reduce the virtual room environment size to facilitate working with the parameters range when working with very large speaker setups. Working with arrangements normalized this way facilitates dealing with automation 
!>  Important, when using the **normalize function or any transform function** you should make a copy of the arrangement prior as there is no undo feature.

---


## Speaker Alignment Compute

![inline](include/SpatRevolution_UserGuide_-041.jpg)

> *★Physical and Virtual speakers after using the compute function.*


^
<br> 
In addition, it can also use the measurements you have entered into the speaker arrangement to compute (calculate and apply) the optimum delays and gains for equidistance of all speakers to the center of reference listener. This is an advanced speaker management technique made easily accessible by a single press of the **Compute** button. 
<br>
<br>
It is a speaker alignment method on a speaker's physical configuration that may not have speakers located in ideal locations. Basically Spat revolution will create virtual speakers after calculating and applying the alignment so all speakers become equidistant to the center of reference. This is a technique preconised when using panning methods that are sweet spot centric such as VBAP and VBIP. The methods will provide very smooth panning on arrangements that have all speakers equidistant to the optimum listening position. 
> It is preferable to do this alignment in SPAT Revolution instead of external processing as Spat will use the computed speaker locations (the virtual speakers) for actually spatializing afterward. 

---

## Panning tips

There are four colours associated with the possible panning types:

- Green : this panning type is valide and functional with the selected speaker array
- Orange : this panning type is somewhat functional, but there certainly is a better solution available. Hovering the panning type with the mouse will display a message to help improve the arrangement
- Bright red : this panning type is not functional with the selected speaker array. Hovering the panning type with the mouse will display a message to explain why it does not work.
- Dark red : this panning type is not functional.
- Grey : Two speakers are located at the same spot : the speaker arrangement is incorrect.

^
<br> 
In the Speaker Config window, we can found information about which pan law to use in regard of our speaker array. As there is many options available in Spat, this simplifies the choice to make.
<br> 
<br> 
For more information about each pan law, check out the section [Panning algorithms](5_Spatialisation_Technology_5_5_Panning_Algorithms.md).
---


## Routing Matrix

As you can imagine routing and patching high density channel counts can get complicated. When it comes to that, the SPAT routing matrix is there to help. You will find it at many points throughout the **Environment Setup** graph.

![inline 30%](include/SpatRevolution_UserGuide_-031.png)

> *★Avoid cable swapping on the loudspeaker setup, use software routing instead.*

^
<br>
The routing matrix is available on hardware input and output for routing  as well as for remapping within some modules input and output. (Input transcode, Master, and Master transcoder)
<br>
<br>
The speaker configuration editor, clear channel labelling and the built-in routing matrix system all help to make the process of signal routing, checking and debugging more straight-forward on location, in the virtual mix and in the studio.


---

# 2.3.2. Channel-based spatialization 		

[.hide-footer]

---

### What are channel-based streams

![left 100%](include/SpatRevolution_UserGuide_-054.jpg)


* Channel based audio stream have channel targets.
* They represent specific loudspeaker or sources in particular location.
* Panning algorithms establishes the render of the virtual scene.

> *★In Spat Revolution, multi-channel input streams are handle as linked multi-mono sources!*


^
<br>
When working with _Channel-Based_ audio stream, each audio channel is associated to a source channel of if you prefer to a loudspeaker in a particular location. Channel-Based mix have a specific target. For exemple, in a standard stereo production, when we record an instrument or a soundscape using a stereo microphone set-up, each capsule is intended to be played on a specific channel. 
<br>
<br>
In common cases, we often deal with input stream that have less channels than our output audio stream (most of the time we deal with mono stream as input sources). To allow these sound sources to be spatialized in our virtual space we use panning algorithms . These algorithms or "panner" can use a variety of different pan law to process the signal. > In Spat Revolution, multi-channel input streams are handle as linked multi-mono sources.
<br>
<br>
The different pan laws available in Spat Revolution are discussed bellow.

---

## Panning methods overview

* Amplitude/Intensity based panning (vector or distance)
* Sweep spot centric vs arbitrarily positioned speakers 
* Stereo, 2D, 3D and arrangement specific.

---

## Stereo exclusive panning law

[.hide-footer]

---

### Stereo Pan

<div style="display:none">
Comment: Need Image
</div>

* For Stereo arrangements only. 
* Standard Pan Law


---

## AB & XY

<div style="display:none">
Comment: Need Image
</div>

* For Stereo arrangements only. 
* Pan laws rom widely used dual microphone techniques. 
* Rendering stereo imaging from an omnidirectional scene.
* Similar to VBAP 2D.

 > *★ AB and WFS are the only channel-based pan laws of Spat Revolution to use a delay to locate a source.*
 
^ 
<br>
These two Panning Types will only become available when a _Virtual Room_ is set to be virtualizing a stereo speaker arrangement - they are pan laws that are derived from widely used dual microphone techniques for rendering stereo imaging from an omnidirectional scene. 
<br>
<br>
**XY Panning** simulates the recording of the sound scene by a pair of microphones in an XY coincident configuration. 
<br>
<br>
**AB Panning** simulates the recording of the sound scene by a pair of spaced cardioid microphones, pointing laterally at azimuths +/- 55 deg. (elevation 0), with a distance of 17 cm between the two capsules. Also known as **ORTF**. Because of the nature of this recording technique, part of the spatialization is based on a delay.  
<br>
<br>
> ★ The aim is to get the same stereo flavour as these dual microphone tracking techniques. Try them on close miked sources or any mono source, to get a realistic stereo image.

---

## AB Technique

![left 30%](include/SpatRevolution_UserGuide_-066.jpg)

[.hide-footer]

---


## 2D exclusive panning law

[.hide-footer]

---

### Angular & PanR

<div style="display:none">
Comment: Need Image
</div>

* Pairwise amplitude panning.
* Legacy pan pot laws from the original IRCAM Spat library.
* When using 2D speaker arrangements only 
* Similar to VBAP 2D.
* PanR (Between 4-8 or 12 speakers)

-

> *★Angular & PanR in Spat Revolution are primarily included for backwards compatibility*

^ 
<br>
These are legacy 2D pan pot laws from the original IRCAM Spat library. They only become available when using 2D channel based streams and are primarily included for backwards compatibility. Angular and PanR are pairwise amplitude panning essentially the same as VBAP 2D described on the next sections. There is a subtle difference however, in the way the panning law changes when moving the source from one speaker to another.

---

### Other specific panning methods

* CSP - Continuous Surround Panning 

> *★Only available for 5 speaker arrangements*

<div style="display:none">
Comment: Need Info
</div>

---

## 2D & 3D panning laws

[.hide-footer]

---

### VBAP

Dependencies:

* Speakers must be _surrounding_ the listening position in 2D or 3D.
* Speakers ideally should be equidistant from the listening position.
* 2D Speakers should be on the same horizontal plane as the ears
* VBAP works best when the listening room is not very reverberant


> *★ Panning law between the closest pair of loudspeaker of a virtual source (2 in 2D, 3 in 3D). Widen a VBAP point source by increasing the Spread source parameter.*


^ 
<br>
Vector Base Amplitude Panning has become one of the more standardized methods for multichannel spatialization. It can reproduce on a 2D or 3D configuration. Its sound is characterized by clearly localisable virtual sound sources. Multiple moving or stationary sounds can be positioned in any direction over the speaker array using this method. In theory VBAP can be used on an unlimited number of loudspeakers and can even be reliable on relatively asymmetric setups.
<br>
<br>
**How does it work?** Traditional VBAP works by manipulating the gain of the signals being routed to the two (in 2D) or three (in 3D) closest speakers to a virtual sound source. VBAP relies heavily on an accurate speaker arrangement model to do this. It triangulates gain vectors mathematically in order to render a virtual object in the physical space and achieves its characteristic 'sharp' focus by using only a few speakers closest to the virtual source location. Additionally it is possible to uniformly extend the traditional VBAP pair-wise (or triplet-wise) speaker picking and activate more of the sound system, effectively diffusing the relationship between individual speakers and sounds using _spread_.
<br>
<br>
> ★ Widen a VBAP point source by increasing the Spread source parameter.

---

### VBIP

* Similar variation to the VBAP technique.
* Same 4 dependencies mentioned for VBAP.
* Improve on VBAP for high-frequency (700 hz +) localisation criteria.


> *★ VBAP and VBIP can easily be compared paying close attention to sharpness in intelligibility to vocal sources for example.*

^Vector Base Intensity Panning is a similar variation to the VBAP technique. It can also reproduce a 2D or 3D immersive sound field with sharply localized virtual sound sources. 
<br>
<br>
**How does it work?** VBIP was designed to improve on VBAP when calculating the high-frequency (above 700 hz) localisation criteria. The selection of which speakers to use to render a virtual sound source is very similar to VBAP, only the amplitude calculations differ. The same 4 dependencies mentioned for VBAP, also apply to VBIP. You will need to listen for quite a nuanced difference between these two panning algorithms. Try to compare how each panning type handles the higher frequency content of your material. 
<br>
<br>
If you struggle to figure out the difference between VBAP and VBIP, think of the different panning laws in stereo. The most used law induce a drop of -3dB at the center and is called "constant power pan law". This can be compared with VBAP. The other very well known stereo pan law is called "constant intensity pan law" and introduce a drop of -6bB in the center. This law can be compared with VBIP.

---

### VBAP and VBIP 2D

![inline](include/SpatRevolution_UserGuide_Panning_7812.jpeg)

---

### VBAP and VBIP 3D

![inline 80%](include/SpatRevolution_UserGuide_Panning_1.png)


![inline 80%](include/SpatRevolution_UserGuide_Panning_2.png)

---

### VBAP, VBIP and ANGULAR Amplitude

![inline](include/amplitude.png)


> *★ Simple schematic showing the gain amplitude curve comparaison from VBAP,VBIP and Angular method on a +/- 30 degree position variation.*


---

### Dualband amplitude panning (DualBandVBP)

The dependencies mentioned in the VBAP section also apply to Dual Band Vector Based Panning.

Both Intensity and Amplitude Vector Based panning has an ideal frequency range of action:

* Localization of low frequencies is better with Amplitude Panning.
* Localisation of high frequencies is better with Intensity Panning.

^
<br>
A hybrid approach of vector based panning has been developed in this way: the Dual Band Vector Based Panning.
<br>
<br>
This panning type merges the two approaches in order to combine the best of both worlds and to reach a better localization. Amplitude panning is applied below the crossover frequency, while the intensity panning is applied above.
<br>
<br>
The crossover frequency has been defined to 700Hz by default.


---

### Layer based amplitude panning (LBAP)

(to be completed)
Layer based amplitude panning could be thought as multiple 2D VBAP layers. The speaker setup is split into several layers, depending on the speaker elevation. The panning used between speakers on the same layer is the VBAP2D. Between these layers, a crossfade is applied between the two nearest layers. The difference between VBAP3D and LBAP is the number of speakers which will be active between the layers: 3 in VBAP versus 4 in LBAP.



---

### DBAP (2D only)

* Alternative for arbitrary systems (not Sweet spot dependant)
* Spatialization method (matrix-based) supporting irregular speaker.
* Equal intensity panning to a loudspeaker array of any size.
* Amplitude weighting based on a distance attenuation model.

-
> *★ DBAP Takes the actual positions of the speakers in space as the point of departure while making no assumptions as to where the listeners are.Speakers can be freely positioned as well*


^ 
<br>
Some panning algorithms are **not** _Sweet Spot_ dependent. Distance-base amplitude panning (DBAP) is one of them. DBAP is useful in a number of practical situations such as concerts, stage productions, installations and museum sound design where the predefined geometric speaker layouts which immersive sound fields rely on, are not possible to establish. 
<br>
<br>
**How does it work?** DBAP localises sounds towards arbitrarily positioned speakers in a space using a matrix based technique. It calculates signal amplitudes according to the actual positions of the speakers in a space, while making no assumptions as to where the listeners are situated. The amplitude calculation known as a weighting is based on a distance attenuation model between the position of the virtual sound source and each loudspeaker. DBAP Extends the principle of equal intensity panning from a pair of speakers to a loudspeaker array of any size.

---

### KNN

* Distance between the virtual source and the K-nearest speakers.
* Amplitude panning over the K-nearest Neighbour speakers.
* Defined by pourcentage.

![left 130%](include/SpatRevolution_UserGuide_-064.jpg)

> ★ The n. Neighbours Spreading parameter defines the number of speakers the source will use. Is is a simple pourcentage of the total number of speakers on the arrangement.

^
<br>
KNN is another panning type that does not depend on a sweet spot to be perceived correctly. It is a version of a 'Nearest-neighbour' interpolation algorithm. These family of algorithms are also used in the fields of complex systems, 3D graphics and network science to name a few.  
<br>
<br>
**How does it work?** An interesting difference between DBAP and KNN is that the user gets manual control over one of the main coefficients in the underlying algorithm. The parameter is called _Nearest Neighbour Spreading_. It sets a maximum limit to the number of speakers that the algorithm can use as neighbours - the parameter becomes available as a continuously variable percentage _for each virtual source_ in a Spat room.
<br>
<br>
 What makes this particularly interesting is that different sources can activate less or more of the sound system dynamically and in a very smooth way. For example, one virtual sound source might seem to pop in and out of individual speakers because the _Nearest Neighbours Spread_ parameter is set a low percentage. For example, on a 10 speaker arrangement :1-10% will use 1 speaker, 11% to 20% 2 and so on. Another sound source could seem diffuse over the entire sound system, because it's spread variable is set to 100%.

---

### SPCAP - Speaker-Placement Correction Amplitude

* Great tools for down-mixing and up-mixing.
* Sweet-spot dependent with wider listening area.
* Speakers must be placed _around_ the listening position.
* 2D speakers should be on the same horizontal plane as the ears.
* SPCAP guarantees conservation of loudspeaker power output across any speaker arrangement.


> *★ SPCAP panning can do a good job of translating surround audio mixes from one speaker configuration to another.*

^
<br>
_SPCAP_ is a 3D panning algorithm which takes its inspiration from VBAP. SPCAP selects not just 2 or 3, but any number of speakers to render a virtual source and weights signal gains according to how much each selected speaker is actually contributing to the overall power output of the speaker configuration. Using this method SPCAP guarantees conservation of loudspeaker power output across any speaker arrangement. Its strengths lie in the down-mixing and up-mixing of virtual scenes from very different channel based speaker arrangements, and of being able to render wider sound sources by using more speakers in a smart way. 
<br>
<br>
**How does it work?** The result will still be sweet-spot dependent although it will be a wider listening area. SPCAP inherits some of the dependencies of VBAP to get successful spatial imaging.

---

### Ambisonic equivalent panning

* Takes ambisonic approach to channel based panning
* Very different behaviour from the VBAP/VBIP pairwise method.
* Emulates encoding and decoding of ambisonic in a single process.


^ 
<br>
In common with the channel based panning types we have covered so far, Ambisonics is a technology that also distributes virtual sound sources in space yet it achieves this in a fundamentally different way. Ambisonics relies on a two step process.
<br>
<br>
**Encoding** Audio sources along with their positional information are wrapped up together using signal mathematics to create encoded Ambisonic audio. Ambisonic scenes are always carried on at least 3 channels of audio. They are not intended to be _listened to directly_ they are intended to be _decoded_.
<br>
<br>
**Decoding** Ambisonic audio signals are unwrapped and the positional information contained within them is decoded _specifically_ for one type of speaker configuration. What we get is an immersive sound field that should accurately render the original spatial composition in 2D or 3D on the specified speaker configuration.
<br>
<br>
Keeping these two steps separate has a number of advantages. Primarily, that of being able to record the encoded Ambisonic audio signals independently of any fixed speaker arrangement. On the other hand, it is possible to "fuse" the two stages of the process together resulting in what appears to be the output of a generalized channel based type of panning. That is the ÆP panning type in a nutshell.
<br>
<br>
**How does it work?** ÆP has certain computational and ambisonic mixing advantages and exhibits very different behaviour from the VBAP/VBIP pairwise approaches. It is up to you to decide whether to work with purely Ambisonic rooms or to use ÆP as a channel based panning law. Both approaches are valid and could be useful.
 
---

### Panning Review

* Stereo Pan, AB, and XY (Stereo only)
* Continuous Surround Panning for 5 Speakers
* Angular (pair-wise panning in 2D)
* PanR  (pair-wise panning in 2D on 4-8 and 12 speakers)
* Distance-based amplitude panning (DBAP 2D)
* Vector-based panning (VBAP, VBIP, DualBandVPB 2D & 3D)
* Layer Based amplitude panning (LBAP)
* Nearest-neighbour amplitude panning (KNN)
* Speaker-placement correction amplitude panning (SPCAP)
* Ambisonic equivalent panning (AEP)


---

## Mid Side (MS) 

<div style="display:none">
Comment: Where do we put MS
</div>


[.hide-footer]

---

# 2.3.3. Binaural methods


[.hide-footer]

---

## 2.3.3. Binaural Technology

* Rendering 3D spatial audio content over headphones!

* Using binaural synthesis, a sound can be arbitrarily positioned around a listener synthesizing the sensory experience.

* Like some other two channel formats such as Mid-Side Stereo, binaurally encoded audio is not compatible with stereo speakers


^ 
<br>
Binaural is a recording and synthesis technique which allow to create an immersive sound scene with the use of headphones. This method is incredibly helpful to deliver an immersive experience to a wide range of people. Binaural recordings (also call native binaural) are created by using small microphones placed at the outside of ears. The ears could be either from real human heads or dummy-heads. By using such recording technique the whole shadow of the head is captured, and thus, its effect on sound perception and position. Such recording formats can be handle in Spat Revolution by using a binaural input module. We can then blend native binaural and synthesized binaural using Spat Revolution with a binaural rooms.
<br>
<br>
The expression “binaural technology” covers various methods of sound recording, synthesis and reproduction which can render 3D spatial audio content over headphones. For instance, binaural field recordings can be made by placing miniature microphones in the ear canals of a listener or of a dummy head (like ' **Kemar** ' or ' **KU100** ') and when played back over headphones such recordings can produce an authentic immersive auditory experience with enhanced spatial aspects. Recent advances in signal processing technology have made it possible to synthesize binaural signals without the need of microphones.
<br>
<br>
Using binaural synthesis, a sound can be arbitrarily positioned around a listener synthesizing the sensory experience  of extended spatialization. Like some other two channel formats such as Mid-Side Stereo, binaurally encoded audio recordings are not compatible with stereo speakers. If a binaural encoded audio file is played on a normal stereo setup, audio will be heard, but it won't sound good. 

---

### Binaural and Transaural

![inline](include/SpatRevolution_UserGuide_Mixing_Binaural_Sources_2.png)

> *★Binaural rendering for headphones (with compensation for near-field effects) or Transaural for loudspeakers.*

---

### Binaural and Transaural

> ★Binaural rendering for headphones (with compensation for near-field effects) or Transaural for loudspeakers.

![right 70%](include/SpatRevolution_UserGuide_transaural.png)


---

### Binaural Synthesis


* Binaural Rooms
* Binaural Monitoring

-

> *★There are two different ways to approach binaural synthesis in Spat Revolution. These two methods serve different usage and workflow.*

^ 
<br>
Binaural rooms takes channel-based sources and output a binaural stream. Each source is binaurally encoded at its exact position in a virtual scene and the reverb is modelled and synthesized binaurally. Thanks to this, binaural rooms result in an excellent immersive experience. 
<br>
<br>
It is the preferred method to use for binaural production content. In the Environment Setup of Spat Revolution, there is a module dedicated to Binaural Monitoring. Its purpose is to monitor any kind of channel based speaker arrangements using headphones. In contrast with binaural rooms, which virtualize each source, binaural monitoring only virtualize each speakers. It's aim to give an impression of how a given spatialization might sound on a particular channel-based system when you are off location.

---

### Ambisonic to binaural



* Ambisonic to Binaural is achieved via channel-base transcode 
* Channel-based stream can easily be monitored binaurally.

-

> *★Choice of appropriate decoding options and channel-based arrangement is critical to good binaural monitoring of ambisonic.*

^ 
<br>
Spat currently doesn't offer a module to transcode ambisonic directly to binaural. Alternatively, it can be done by transcoding an ambisonic stream to a channel-based arrangement and then use a binaural monitor module in this channel-based stream. See the Ambisonic in Spat Revolution section for more information

---

### Binaural on loudspeaker


* Binaural 2 channels are not compatible with stereo speakers
* Transcode module provides transaural output to convert binaural to stereo.

-

> *★To transcode binaural to transaural in Spat Revolution, you can either use input or master transcoding module.*

^ 
<br>
By default, binaural streams and files are not compatible with stereo speaker systems. If we took a closer look to a listening experience with headphone, we can quickly identify that the main difference between headphone and loudspeaker is that, with headphones, the left ear only hears the left signal and vice versa. While on loudspeaker, there is crosstalk between left ear and right signal. This is these crosstalk that make binaural incompatible with speakers. Still, there is a workaround that make binaural experience compatible with loudspeakers. 
<br>
<br>
It is called _transaural_. The idea is to cancel the crosstalk signals with some additional processing. It is then possible to make stereo experience a bit more immersive but it is critical that the listener has to be exactly placed at the sweet-spot.

---

## HRTF

[.hide-footer]

---

### Head-Related transfer function (HRTF)

![left 100%](include/SpatRevolution_UserGuide_Pref_HRTF.png 'size=400x')

* Default Generic Kemar HTRF.
* Manage HRTF in the preference pane.
* Significant role in the way we localise sounds as we are all unique.
* Math model of the filtering effect caused by a listener's body.

^
<br>
HRTF is an abbreviation for Head Related Transfer Function. The function is a mathematical model of the filtering effect caused by a listener's own head, external ear and torso. This filtering plays a significant role in the way we localise sounds around us and is unique to every individual.
<br>
<br>
When synthesizing binaural , a perfect result could be attained by rendering through the exact HRTF that matches the body filtering effect of an individual. In practice this is not easily done, so Spat Revolution offers many choices of pre-analysed HRTF profiles which you can apply for monitoring and encoding binaural audio. 
<br>
<br>
Spat Revolution offers HRTF profiles which you can apply for monitoring and encoding binaural audio. You can manage the selection of HRTF profiles in the Spat Revolution Preferences where you will find a number of different profiles including the option to load your own personalized HRTF. The default HRTF provided is the Kemar dummy head model, which is often used as an all round generic head and shoulder filter. 
<br>
<br>
The included HRTF profiles in Spat Revolution are taken from a number of large scale laboratory research projects where measurements were taken on many individuals. The chances are that one person's ears may sound more natural to you than others. For a quick way to monitor binaural, you should try to find a profile that you feel most comfortable with when monitoring your virtual scene on headphones.
<br>
<br>
Go ahead and try to find a profile that you feel most comfortable with when monitoring your virtual scene on headphones. As an example, the KU100 Neumann HRTF widely found and used in 360/VR pipeline and VR SDK (Google, YouTube, etc.) can be simply searched in the database, downloaded, and included in your workflow. Choosing it as the default HRTF will make sure it is set every time you use a binaural room on monitor modules.  
<br>
<br>
If you are providing a 3D in-ear monitor mix for a performer or a visitor to an installation, try to find an HRTF that suits them best. This can be fun. If you are not comfortable listening through someone else ears - which is understandable - you could look into creating a personalized HRTF from your own head and upper torso measurements. One reality is that getting a more truthful and reliable monitoring experience, with a far more natural sense of space and direction can be achieved with your own individual / personalized HRTF!  There is already a number of services that can create HRTF profiles taken from laboratory measurements. If you decide to do this, for yourself or someone else, then you can add the personalized profile to the list of HRTF Manager. In fact you can import any HRTF in SOFA format to the Spat Revolution database, making Spat Revolution a very flexible solution for binaural monitoring and rendering.
<br>
<br>
!> _An imported HRTF profile should be in SOFA format and should match the sample rate for your project. It is preferable to use a "SimpleFreeFieldSOS" IIR type of HRTF_
\* The profiles come from the "LISTEN" , "CROSSMOD" and "BiLi" databases.


---

### HRTF Managements

![inline 70%](include/SpatRevolution_UserGuide_HRTF_Manage_KU100.png 'size=600x')


^ 
<br>
Using binaural audio automatically means dealing with HRTF and managing them. In Spat Revolution, you can do this in the preferences menu in the HRTF section and accessing Manage HRTFs. You will see in the HRTF section your current default chosen profile (which is default to Kemar). Choosing the Manage HRTF section will bring you to a database list that contains locally available and optional downloadable HRTF. When downloaded (or local on your computer) the concept of include / exclude allows you to decide which HRTF are showing as available when using a binaural room or binaural monitoring module in Spat Revolution.

---

### Importing personal HRTF - SOFA file

![inline 130%](include/HRTF_Import_Success.png 'size=600x')

^ 
<br>
If you have the pleasure to have your own HRTF, you can simply import them to Spat Revolution with a few steps simple steps. Please ensure that your HRTF is using a SOFA file format and is diffused field equalized. Diffused equalized refers to the direction-independent component in the HRTF removed. This direction-dependent component is referred to as a DTF version. (Direct Transfer Function). SimpleFreeFieldHRIR or SimpleFreeFieldSOS IIR. 
<br>
<br>
> *★Preferred Convention: SimpleFreeFieldSOS IIR.* Ideally, your file name ends with _SampleRate.SOFA_. With this file name structure, Spat Revolution will import all your HRTF as a single entity with various sample rates available. Otherwise, each sample rate will be imported as a separate HRTF which is not as convenient.  File examples:
<br>
<br>
_"My HRTF name”_44100.sofa_
_"My HRTF name”_48000.sofa_
_:My HRTF name”_96000.sofa_


---

## Binaural algorithms

[.hide-footer]

---

### Normal binaural mode

This mode uses the selected HRTF in order to recreate the sound field.
---

### Near-field binaural

HRTF are generally measured at 1 or 2 meters of the listener. In the reality, the HRTF are changing with the distance between the source and the listener, especially when sources are closed. The Near Field Binaural tends to recreate close HRTF, with an additional filter set applied.

---

### Spherical head model

This binaural synthesis simulate the head like a rigid sphere, instead of using HRTF. An additional parameter provide the control of the head radius. As this model doesn't use HRTF, this synthesis consumes less CPU. However, the localization is clearly less precise.

---

### Snowman model

This synthesis is the improvement of the Spherical Head Model. 
Besides the head reflexions, torso ones are simulated, like two spheres one on the top of the other. Hence its name, "snowman model".

---

### Head scale

The parameter "head scale", available for the four binaural algorithms, allows to adapt the head size to the listener. This will adjust the inter-aural time and level differences.

---

## Binaural Monitoring Module
(to be completed)
![inline](include/SpatRevolution_UserGuide_-050.jpg)

[.hide-footer]

^
<br>
In the _Environment Setup_ of Spat Revolution, you will find a module dedicated to Binaural Monitoring. Its purpose is to monitor any kind of speaker setup using headphones and binaural encoding. This can give you an impression of how your spatialization might sound on a particular channel based system when you are off location.
<br>
<br>
You can add a Binaural Monitoring Module by clicking on the <code>+</code> icon of the Binaural Monitoring row towards the bottom of the **Environment Setup** graph. The module is very simple to use. It will automatically detect the type of channel based audio stream you connect into it.
<br>
<br>
The Binaural Monitoring module works by virtualizing each speaker, not each source, so any real world speaker phenomena will be reflected in the binaural rendering. For example, a virtual source positioned in the centre between two virtual speakers will be rendered with the same 'phantom speaker' in the binaural monitoring as in the physical world, because there is no virtual speaker at the centre point either.
<br>
<br>
To listen to the binaural stream on headphones, you should select the HRTF you would like to use for the encoding, and connect the output from the module to a dedicated output module at the bottom of the graph. The output should be routed to the headphone monitor outputs of your audio hardware.

---

### Listener Position

![inline](include/SpatRevolution_UserGuide_-058.jpg)

> The dummy head is only visible for sweet spot dependent panning types
> The Listener Position can be moved in a Spat Revolution room.

^
<br>
The impression of positioned audio which is rendered on a speaker array is generally successful when a listener is situated in the optimum position to perceive it the so-called _Sweet Spot_. Thanks to the popularity of stereo sound, people tend to know that if you want to hear a good a stereo image, you should place yourself in front of the two speakers and stand somewhere in the middle. That's a good way to describe the _Sweet Spot_ to an audience or client. In more complex speaker arrangements the _Sweet Spot_ is usually considered to be the area that all the speakers (or sound emitters in a virtual space) are pointing to. It has the cartesian coordinates of (0,0,0) in relation to the speaker positions. In Spat Revolution the optimum listening area is represented by the dummy head and the inner circle that surrounds it.
<br>
<br>
The dummy head indicates the _Listener Position_. In SPAT the _Listener Position_ is actually a bit more useful than just an indication of the Sweet Spot. In general it is useful for getting some bearings in the spatial composition. Knowing which direction the listener position is facing, helps you understand the spatial image and place sources correctly. 
<br>
<br>
For example, a train audibly approaches from the left in an ambisonic field recording you are working with as a source, but it visually approaches from the right on the video footage you are editing to. You can use the listener position as a reference point to transform the field recording correctly so that it correlates to what's happening on screen. Also, when working in 'stage' oriented spaces, the listener position in a SPAT Room will help you compose a scene with the correct relationship to the front, back and sides of the space. It also provides a method for giving a sense of distance to a sound source by placing virtual sound objects closer or farther away from the listening position. The internal distance perceptual cues, such as air absorption, doppler and gain drop are all calculated in relation to the _Listener Position_.
<br>
In certain advanced situations which might combine position tracking systems with realtime binaural audio it is even possible to transform the _Listener Position_ in SPAT. One application of this might be to give the sensation of getting closer to a sound emitter inside a virtual scene for a headset wearing participant at an interactive VR installation.


---

### Head-tracking

![inline](include/SpatRevolution_UserGuide_-060.jpg)


---

### Head-tracking

> *★Listener position in Spat Revolution room comes of six degrees of freedom (6DoF) *

![left 130%](include/SpatRevolution_UserGuide_ListenerPosition_Tracking.png 'size=400x')
 
^
<br>
Talking about binaural audio and listening positon, each SPAT Revolution room have the ability to change the position of the listener hence ultimately tracking this position. All parameters can be controlled via OSC and can alternatively be mapped to a real-time tracking beacons using RTTrPM protocol.

---

# 2.3.4. Wave Field Synthesis (WFS)

[.hide-footer]


---

# 2.3.4. Wave Field Synthesis

> *TO BE DEFINED AS THE FUNCTION BECOMES AVAILABLE*


---

# 2.3.5. Scene-based in Spat Revolution
 	
[.hide-footer]

---


Panning and recording base!!!

Mid-Side … intro to Ambisonic...


[.hide-footer]

---
	              
## Scene-based streams
### Introduction to ambisonic

![left 40%](include/SpatRevolution_UserGuide_-043.jpg 'size=200x')


* Scene-based format
* Capture and render 2D or 3D immersive sound fields
* Does not carry a speaker signal but an ensemble of direction
* Portable and played on a number of speaker arrangements based on the chosen decoder.


^ 
<br>
Simply put: Ambisonic is a specific method for creating, capturing and playing back spatial audio. It is radically different from other surround techniques as the technology is capable of reproducing a spherical representation of sound where the directional information of a source is located in a 3D sound-field.
<br>
<br>
Ambisonic is also both a recording and a spatial synthesis technique, where one can capture the full environment in 3D sound through the use of so called A or B-format microphones such as the: Soundfield SPS200, Røde NT-SF1, Sennheiser Ambeo, Coresound TetraMic and more. Alternatively, a sound field can be synthesized from any mono, stereo and multichannel sources to Ambisonic, constructing a virtual 3D sound environment by placing the sources at locations in a virtual 3 dimensional field.
<br>
<br>
Ambisonic is a technology to capture and render 2D or 3D immersive sound fields. Its invention goes back to the '70s, due to the research work of Michael Gerzon and Peter Craven. At its root, ambisonic is really just an extension of the MS matrix of a stereo signal. When this stereo signal is expressed as a left/right stream, it describes an array of points (the left and right speakers). When it is encoded in MS, it describes an ambiant signal (mid element of the matrix) and one direction (Side element). So, ambisonic, as opposed to other surround and spatial techniques and methods, does not carry a speaker signal but an ensemble of direction (X, Y and Z axis for exemple). It is an encoded audio signal that has to be decoded to the speaker signals. This encoding / decoding scheme has the advantage of being very portable and flexible since one is not bound to a specific speaker setup. i.e you can have your ambisonic mix played on a number of speaker setups, for instance Quad, headphones (binaural), 5.1, 6, 8, 7 speaker etc. based on the chosen decoder. Because of these very specific properties, an ambisonic system is called a scene-based format.

---

### First order ambisonic (FOA)

![right 30%](include/SpatRevolution_UserGuide_-045.jpg 'size=300x')


* W: it is the common signal
* X: it is the front-rear axis
* Y: it is the left-right axis
* Z: it is the up-down axis

> *★The simplest form of ambisonic format, called B-format, is described as above.*

^ 
<br>
In the simplest form of Ambisonic - the 1st order ( also called **B-format** ) - only 4 channels is needed to represent a full 3D sound. The 4 channels or spherical components W, X, Y and Z resemble the pressure patterns found in an omni microphone (W) and three figure-of-8 microphones for left/right (Y), front/back (X) and up/down (Z) as depicted in Fig.1.
<br>
<br>
In practice, the B-format is a mixing format. Ambisonic microphones output a different signal arrangement called "A-format". First-order ambisonics microphones simply consist of four capsules. The "A-format" is the raw output of such microphones, before any encoding. One last FOA format exists, and aim to be a storage/output format. It is called C-format (or UHJ). This particular arrangement allows getting an output stream compatible with mono and stereo diffusion.



---

## Higher order ambisonic (HOA)

^ 
<br>
In Spat Revolution, an ambisonic stream can be up to seventh order. By increasing the order of an ambisonic stream, we also increase the precision of source localisation. For comparison purpose, if B-format describes one common signal and three directions (four channels), a 3D/7th order HOA describe one common signal and 63 direction (64 channels). 
<br>
<br>
It highly increases the sense of space and the immersive effect of the sound stage. This improvement in sound comes at the cost of a much more intense CPU processing. It is thus recommended to choose the order that suite the need of the project.

[.hide-footer]

---

### Practical use of ambisonic in Spat Revolution

^ 
<br>
Rendering to ambisonic format is a good way to render immersive audio production and decode them on the fly according to the speaker arrangement needed. This mean that you can store an "agnostic" file which is not dependent on any diffusion standard. This is a good alternative to channel-based immersive stream because they do not support very well up & down-mixing.

[.hide-footer]


---

### General ambisonic transcoding options

Ambisonic formats can take various forms. To deal with them all, Spat Revolution includes a comprehensive ambisonic transcoder. The input configuration *have to* match the input stream

---

### Ambisonic type

Spat Revolution transcoder can handle:

* A-format
* B-format
* C-format (UHJ)
* HOA

---

### Dimension

Dimension can be either 2D (no elevation) or 3D.

---

### Order (HOA only)

The order can be set from one to seven.

---

### Normalization

<div style="display:none">
Comment: _need some more reading_
</div>


* SN2D
* N2D
* FuMa
* MaxN

---

### Sorting

The sorting define the order of the different channels of the input stream.

* ACN
* SID
* FMH

<div style="display:none">
Comment: 
// to complete : https://en.wikipedia.org/wiki/Ambisonic_data_exchange_formats#Furse-Malham 
// https://mhacoustics.com/sites/default/files/Eigenbeam%20Datasheet_R01A.pdf
</div>

---

#### Yaw angle

This allows to rotate the sound stage by steps of 90°.

---

### Using ambisonic recording...

[.hide-footer]

---

### ...With channel-based and binaural room

[.hide-footer]

---

### A-format input

^ 
<br>
Ambisonic recording usually comes in A-format. Each ambisonic microphone have its own A-format to B-format conversion. Spat Revolution handle some industry standard microphones. To transcode a A-format to use it into a channel-based or binaural room, you need to set up an input transcoder. 
<br>
<br>
Select "A-format" as input format (here the microphone model can be chosen) and "Channel-based" as output format. If you are decoding into a channel-based room, you may want to match the format of this room. In the case of a binaural room, "Full Uniform" type speakers arrangements are good options.
<br>
<br>
Behind the hood, the A-format to channel-based operate in two steps: * A-format is decoded to B-format * B-format is decoded to channel-based

[.hide-footer]


---

### ...With ambisonic room

[.hide-footer]

---


### Ambisonic Transcoding
#### Default transcoding

When patching an HOA or B-Format input to a sources, or a HOA room to a channel-based output, a transcoder will be automatically inserted. This transcoder will, by default, be set to the Sloane speaker arrangement corresponding to the HOA order, and, will select an energy-preserving decoder.


---

## HOA Transcoding presets
[.hide-footer]

---

### Spat Ambisonic Format

[.hide-footer]


---

### Dealing with A-format

![left](include/SpatRevolution_AFormatPreset.png)

> *★You can simply choose the needed decoder in the input transcoder.*

^ 
<br>
A-format is a 4-channel audio stream. It is the RAW output of a first-order ambisonic microphone, so it has not been encoded to ambisonic yet. Because each manufacturer has their own strategy to create such microphone, we have almost as many transcoder as a-format microphone builder. Spat Revolution comes with a comprehensive list of A-Format transcoder, including Sennheiser Ambeo, Soundfield, DPA, Oktava etc.


---

### Dealing with AmbiX

![right](include/SpatRevolution_HOApreset.png)

^ 
<br>
Ambix is becoming the most used and spread out B-format in the production world. Inside transcoder blocs, there is some ambisonic presets that allow to quickly transcode the output of an ambisonic room, for example, into an B-format stream.


---


## Transcoding method
[.hide-footer]

---


### Projection

* Projection decoding is also sometimes called 'sampling ambisonic decoding' (SAD).
* It is the simplest form of ambisonic decoding.
* It samples the virtual panning function at the loudspeaker directions.

^
<br>
SAD is optimal for loudspeakers arranged as t-design layouts, with $t \geqslant (2N+1)$ ($N$ being the Ambisonic order). Typically, the SAD should only be used for 2D loudspeaker layouts, i.e. arranged regularly in a circle. Avoids this decoder for 3D setups. _to be completed_
<br>
<br>
*What is a t-design layout?* To keep it really simple, t-design is a mathematical way of constructing sphere perimeters or circle surface with an array of point that is homogenous. In 2D the point simply put on a circle and are evenly spaced. In 3D, things get much more complicated many t-design point layout exist. In Spat Revolution, we choose to use the method used by the mathematician Sloane for our speaker layouts.

---

## Regularized pseudo-inverse

* The pseudo-inverse decoder, or 'mode-matching decoder' (MMAD)
* Suitable for both 2D and 3D.
* Uniform loudspeaker arrangements.
* Based on a pseudo-inverse of the re-encoding matrix


^
<br>
The pseudo-inverse decoder, or 'mode-matching decoder' (MMAD), is suitable for both 2D and 3D.
It is based on a pseudo-inverse of the re-encoding matrix. MMAD is well-behaved for regular loudspeaker arrangements. It can also give good results with slightly irregular setups.
However it can become unstable with strongly irregular setups, i.e. it can completely blow up the speaker feeds. So, be careful. With the '/info' message, you obtain the conditioning number of MMAD.
<br>
<br>
This number gives you an estimate of how well-balanced the system is. A conditioning number close to 0 dB is excellent. Values less than 10 dB are usually quite acceptable. With values higher than 20 dB, the decoding can become problematic (or dangerous).
<br>
<br>
The regularized pseudo-inverse decoder or 'regularized-mode-matching decoder' (RMMAD) is somehow similar to MMAD, however it uses a regularization factor for stabilization of the pseudo-inverse. This regularization factor (alpha) varies from 0% to 100%. A value of 0% provides results similar to MMAD. A value of 100% generates even energy distribution, i.e. results similar to EPAD. Intermediate values of alpha allow to 'blend' MMAD and EPAD.

---

## Energy preserving

* Typically recommended transcoding method
* EPAD suitable for 2D and 3D HOA
* Can cope with any kind of loudspeaker arrangement
* EPAD uses a regularized matrix inversion


^
<br>
EPAD (Energy preserving ambisonic decoding) and AllRAD (All-round Ambisonic decoding) are other HOA decoding methods suitable for 2D and 3D HOA, and they can cope with any kind of loudspeaker arrangement. These decoding methods always work, as soon as there are enough loudspeakers; they are always feasible and by nature numerically stable.
<br>
<br> 
EPAD uses a regularized matrix inversion such that the decoded energy is preserved even with non-uniformly arranged arrays (and even for directions with only sparse loudspeaker coverage).
<br>
<br>
EPAD is the default method in spat5 (and the one we usually recommend).

---

## AllRAD

'All-round Ambisonic decoding' (AllRAD) is designed in two steps. First, an optimal virtual loudspeaker layout using t-design arrangement is considered (for which the SAD is optimal); Secondly, the signals of these virtual loudspeakers are mapped to the real loudspeakers via VBAP.

---

## AllRAD+

*  Combines AllRAD and SAD.
*  Improved All-Round Ambisonic Decoding (AllRAD+)

^
<br>
'Improved All-Round Ambisonic Decoding' (AllRAD+) combines AllRAD and SAD. Constant energy that is achieved for the idealized virtual loudspeaker setup in AllRAD is corrupted by the VBAP stage as, per loudspeaker pair, all virtual sources are superimposed linearly instead of energetically.
The prevailing linear superposition increases the energy wherever the loudspeaker spacing is large. Roughly, at such directions AllRAD doubles the energy, whereas it is halved at directions with dense loudspeaker spacing.
<br>
<br>
Conversely, SAD might lose all energy where the loudspeaker spacing is large and roughly doubles it where the loudspeaker spacing is dense.
<br>
<br>
AllRAD+ tries to solve this issue by combining (i.e. mixing) SAD and AllRAD. The loudness variation of AllRAD+ is competitive with EPAD and its angular mapping resembles AllRAD.

---
## Transcoding presets
### Dealing with A-format
### Dealing with Ambix
to be completed

--

## Decoder Type
[.hide-footer]

---

### Basic decoder type

This is the standard way to decode ambisonic and no optimization is applied.

---

### InPhase decoder type


---

### MaxRe decoder type

to be completed

---

### BasicMacRe decoder type

The low end of the audio content is not optimized, but a MaxRe method is applied to the high end. The crossover frequency is by default set to 700Hz and can be adjusted.

---

### MaxReInPhase decoder type

---

### InPhaseMaxRe decoder type

As phase optimization is more efficient in the low frequencies, and energy optimization is prominent in the high frequencies, this method take this phenomena to its avantage by splitting the signal in two frequency band. The crossover frequency is by default set to 700Hz and can be adjusted.

---

### ...To a speaker array

[.hide-footer]

---

### ...To a headphone

There is no direct ambisonic to binaural transcoder, but you can easily achieve this. Here is the recommended signal flow:

* Wire your ambisonic room or input into a master transcoder.
* In the transcoder, choose a regular speaker layout, like the "Full Uniform 30°" as output
* For transcoding methods: we recommend the Pseudo-inverse method in "basic" type.
* Then wire the master transcoder to a binaural monitoring bloc.
* Choose your preferred HRTF

<div style="display:none">
Comment: @todo
</div>

---

* Encoding Spherical Array Microphone recordings
* Decoding HOA audio
* Transcoding HOA audio

---

!> From Spat Revolution User Guide

<div style="display:none">
# 4.6 The Ambisonic Method

One of the challenges facing spatial audio designers is how to spatialize and mix when the full installation is not available to mix on. The other related problem is how to re-spatialize a virtual scene mixed for one type of speaker layout, onto a different one. Spat Revolution can provide solutions to these problems.

In order to get a rough idea of how a spatialized scene might sound on a particular speaker configuration - including the gaps between the speakers, and the characteristic of a chosen panning type - then the binaural 3D headphone monitor module can be used. It can give a headphone representation of a channel based virtual scene. It has its limitations though so the binaural monitor module should not be relied upon for all mix decisions. It is there as a quick way to 'dip' into the virtual scene but only has the spatial resolution of the number of speakers in the channel based stream.

A better way to get a high resolution 3D audio image would be to create a binaural room in parallel with a channel based room. This will _binauralize_ the sources and their virtual acoustics in a room with no speakers - this is the best binaural experience Spat Revolution provides - although of course it is still limited to headphones only (see section 5.1).

Perhaps the most practical solution, comes from the ambisonic technology which is at the heart of Spat Revolution, and in fact behind the binaural rendering just described. Ambisonics, as we are about to discover, is an **encoded** audio format that gives us the possibility to **decode** consistent 3D spatial information onto any channel based / speaker compatible format. Because Spat Revolution is fundamentally a High Order Ambisonics engine, it gives a designer the possibility to keep working on the spatial parameters of a complex virtual audio scene and monitor on whatever speaker or headphone setups she might have access to - such as binaural, 5.1 surround, simple Quad, stereo and so on. The spatialization should translate more or less intact after decoding. Of course, there's still tuning work to do in practice, but it is much better than imagining how things are going to sound, and further more - is a very interesting application of an audio technology with quite a legacy behind it. Time for a quick introduction to Ambisonic technology.


Simply put: Ambisonic is a specific method for creating, capturing and playing back spatial audio. It is radically different from other surround techniques as the technology is capable of reproducing a spherical representation of sound where the directional information of a source is located in a 3D sound-field.

Ambisonic is also both a recording and a spatial synthesis technique, where one can capture the full environment in 3D sound through the use of so called A or B-format microphones such as the: Soundfield SPS200, Røde NT-SF1, Sennheiser Ambeo, Coresound TetraMic and more. Alternatively, a sound field can be synthesized from any mono, stereo and multichannel sources to Ambisonic, constructing a virtual 3D sound environment by placing the sources at locations in a virtual 3 dimensional field.

![](include/SpatRevolution_UserGuide_-045.jpg)

In the simplest form of Ambisonic - the 1st order ( also called **B-format** ) - only 4 channels is needed to represent a full 3D sound. The 4 channels or spherical components W, X, Y and Z resemble the pressure patterns found in an omni microphone (W) and three figure-of-8 microphones for left/right (Y), front/back (X) and up/down (Z) as depicted in Fig.1.

Ambisonic as opposed to other surround and spatial techniques and methods does not carry a speaker signal. It is an **encoded** audio signal that has to be **decoded** to the speaker signals. This encoding / decoding scheme has the advantage of being very portable and flexible since one is not bound to a specific speaker setup. i.e you can have your ambisonic mix played on a number of speaker setups, for instance Quad, headphones (binaural), 5.1, 6, 8, 7 speaker etc. based on the chosen decoder.

When Ambisonic is played back on speakers all the speakers contribute to the directional content, what one is hearing is not the sound coming from a specific speaker but from a specific direction.

![](include/SpatRevolution_UserGuide_-047.jpg)

Overview of a 5 HOA 3D Ambisonic File created by Tine Surell Lange

Ambisonic was originally developed by the late British mathematician and sound engineer Michæl Gerzon and others in the 1970s. Although it was a commercial failure at the time, this very powerful spatial technique has since been advanced greatly by a number of composers, sound designers and researchers. With the introduction of Virtual Reality, fast decoders and related technology, Ambisonic is getting a new renaissance being a perfect format for such applications.

If you want to learn more about Ambisonic and its mathematical foundation here
are some good starting points:

[https://www.researchgate.net/publication/280010078_Introduction_to_Ambisonics](https://www.researchgate.net/publication/280010078_Introduction_to_Ambisonics)

[http://flo.mur.at/writings/HOA-intro.pdf](http://flo.mur.at/writings/HOA-intro.pdf)


# 6.7.9 B-Format Room

This is a First Order Ambisonic (FOA) room which is correctly suited for mixing B-Format Ambisonic signals. B-Format is 4 channel interleaved Ambisonic format, which is already widely used as a 3D audio format in the audio industry, as it can be decoded quickly and efficiently in realtime. If you are producing content that is intended for realtime decoding in B-Format, you can work in a B-Format Room.

The output configuration is preset for B-Format Room, although it is possible to change to 2D or 3D.

![](../include/SpatRevolution_UserGuide_-120.jpg)

In the classic Furse-Malham (FuMa) sorting system for 1st order is: WXYZ. W is the mono sum and it is carried on channel 1. In the ACN channel order convention a 1st order signal is arranged as: WYZX.

# 6.7.8 High Order Ambisonic Room

One of the most straightforward methods to start working with HOA spatialization in a signal flow is to connect input sources directly into an HOA Room. To convert a Room to be HOA, you select High Order Ambisonic as the _Output Configuration Stream Type_.

All inputs to a Room must be in some kind of Channel Based format, even when it is an Ambisonic or Binaural Room. That is the workflow at the time of writing (Spat Revolution v1.1). This makes most intuitive sense, when using Ambisonic format inputs as pre-encoded "3D sound field" type inputs into a room. You cannot just add them into an HOA room, even though they may be HOA format. Why is that?

This is because Ambisonic audio always needs to be _decoded_ into a channel based format to hear the spatialized audio on speakers ( as we have mentioned a few times already). And so in a virtual room, an Ambisonic source needs to be decoded to a _virtual_ speaker configuration. The choice of what virtual speaker configuration you decode the Ambisonic audio to, will influence the way the source's direct signals will sound and its sound will be altered by the way it interacts with the Virtual Room Acoustics. If it is a 1st or 2nd Order B-Format source, then a Cube configuration for 3D or an Octaphonic for 2D is usually a good choice. The important thing to keep in mind, is that a higher order of Ambisonic encoding, will sound more accurate on a higher density channel-based configuration - and if the source Ambisonic encoding is 3D, then you really should choose a 3D type of channel configuration.

!> _Ambisonic encoded audio is not intended to be listened to without decoding_

The other important thing to keep in mind, is that by decoding Ambisonics to a vir tual Channel Based configuration, allows for some very special transformations and re-designing possibilities of the original Ambisonic source. When a B-Format source becomes an arbitrary configuration of virtual emitters in the virtual Room, the ambisonic sound-field becomes a group that you can manipulate and transform using all the source parameters - especially, the barycentric source parameters which are really useful for rotating and transforming the original sound field in many ways (see section 9.9).

> ★ Ambisonic encoding is a convenient way to share and archive spatial sound mixes

The output from an Ambisonic room must always be _decoded_ into a channel based stream in order to hear the resulting spatial image (see section 4.7 introduction to Ambisonic). But even though it is not speaker compatible, it is still an audio data stream - so therefore it is quite possible to record and HOA stream to disk without decoding. This is a powerful way to work, as the HOA format encodes full sphere spatial information which can then be decoded/transcoded at a later stage.

![](../include/SpatRevolution_UserGuide_-118.jpg)

In an HOA Room, the Order and other Ambisonic encoding parameters can be changed at the output configuration of the room very easily, by selecting a different value pull down menus. When you have correctly set up a speaker compatible decoding method for the HOA stream coming out of a Virtual Room, you should clearly hear the difference in focus and the way that the Artificial Reverberation behaves as the Order goes up. Do not be complacent about the simplicity of the HOA interface. There is plenty going on under the hood but Spat makes it feel simple to explore how different Ambisonic Orders sound. Similarly, other encoding options are available to apply and listen to directly.

An HOA Room simulates many different Ambisonic decoding options in realtime. When you decode (or Transcode) an HOA Room output into a Channel Based or Binaural stream, you will be able to hear how different Ambisonic encoding and decoding options (such as Method and Type) will sound. The topic of Ambisonic decoding options such as Type, Normalisation, Sorting and Method is a particularly large one but in the end, it comes down to how the sound field will come across and this involves listening. Similar to how Sommeliers get to know the nuances of wine by opening lots of bottles, the best way to get to know Ambisonic options and understand for yourself how they affect the sound, is by decoding and listening on different setups. And perhaps also digging into some of the literature you will find online.

One thing we can already guide you in, is how each Order affects spatial precision. This knowledge may be beneficial to understand when you are rendering and mixing Ambisonic sound fields. The precision with which a source can be localized in Ambisonics is directly linked to the Ambisonic Order. Sources encoded as first order (FOA or B-Format) can be quite diffuse in their localizability when decoded. Higher Orders, such as 3 or 7 can render precisely localisable point sources in 3D. The cost is in computation and increasing audio channel count ( see Section 6.45 ).

Some types of source material such as ambience or field recordings can benefit from the more immersive feeling of lower Orders, but point sources may need encoding in higher Order to get a more localizable result.
</div>

---

# 2.4. Room effects and the source objects  

---

# 2.4. Room Effects and Source Objects

* 2.4.1. Low-level and high-level control of Room Effects

* 2.4.2. Source parameters review 


---

# 2.4.1. Room effect 

> *★This is no ordinary reverb*

![left 30%](include/SpatRevolution_UserGuide_-142.jpg)
 
^
<br>
Each _Virtual Room_ in Spat can have its own artificial reverberation. Reverberation is a very important element in the psycho-acoustic perception of localized sources and immersive sound fields. 
<br>
<br>
The reverb processor in Spat is a multichannel algorithmic 3D reverb based on feedback delay networks. The Spat reverberation engine is designed to synthesize the experience of the virtual sources and the listener all being placed within the same virtual acoustic space. 
<br>
<br>
Virtual spaces can be tuned, scaled and stored.  Open the _Artificial Reverberation_ graphical editor by clicking on the ( **R** ) index at the bottom of the list of Sources in the left side panel of the Room, or entering a room directly from a tab in the top _global bar_.
<br>
<br>
Internally, the Spat Revolution reverb engine models many technical acoustic parameters, but the user interface has been simplified a great deal, to make artificial reverb design more straightforward and functional.

---
## Spat per-source processing architecture 

* Directional early reflections 
* Diffuse reverberation 
* Per-source perceptual controls 
* Format agnostic representation 
* Library of “Pan” modules 
* Extensible: immersion with height


---

## Reverb structure

> *★Spat per-source processing architecture*

![inline](include/SpatRevolution_Reverb_Schema.png)
![inline](include/SpatRevolution_UserGuide_RoomEffect_1.png)
![inline](include/SpatRevolution_UserGuide_RoomEffect_2.png)

^ 
<br>
**_Early_** refers to _Early Reflections_ stage of the Room response. It is one of the most significant stages involved in our rapid aural perception of spatial properties and sound source localisation.  
<br>
**_Cluster_** refers to a secondary iteration of room response reflections and is quite significant in the cognition of room acoustics. 
<br>
<br>
**_Tail_** refers to the diffuse reverberations that eventually decay in a direct relationship
with the size and reflectivity of an acoustic space. The tail section of a reverb does
not contribute much to the localizability of a sound source in a space, but instead
gives a sense of depth and ambience.

---

## Reverb General

![inline 40%](include/SpatRevolution_UserGuide_-150.jpg)

* Standard and High density 8x8 (standard) or 16x16 size (high)
* Size meta-parameter for quick size of the virtual room
* Reverb start of the reverb tail.
* Reverb Gain and Factor

> *_Reverb Enabled_ - Toggles the tail reverberation engine for the room.*

^ 
<br>
**_Reverb Density_**  Toggles between Standard and High density will affect the quality of the reverberation. Internally, spatial variations are computed using a kind of 2D-network of reverbs, and this setting toggles between an 8x8 (standard) or 16x16 size (high). The choice of which sounds best is left up to you, as this depends on the source material at hand, although it must be emphasized that the high density setting consumes a little more CPU and that the colour and the character of the reverb can be altered by this setting, particularly at some extreme parameter setting combinations.  
<br>
**_Size_** This is a meta-parameter that takes care of varying several other parameters in order to quickly set the equivalent size of the virtual room, adjusting early, cluster and tail reverb parameters to match the room characteristics.
<br>
<br>
**_Reverb Start_** Reverb start sets the duration between the direct, dry source signal, and the first late reflections, or start of the reverb tail.  > Please note its value can never go below that of the cluster minimum time as the reverb tail is fed with a signal derived from the cluster section. **Reverb Gain** **Reverb Factor**

---

## Perceptual Factors

![inline](include/SpatRevolution_UserGuide_-152.jpg)

* Reverberance the time taken by late reflections to vanish into silence.
* Heaviness, the relative decay time of low-frequency content.
* Liveness, the relative decay time of high-frequency content.

^
<br>
**Reverberance**; _Reverberance_ is tightly related to overall decay time of mid-frequencies, which in turn is the time taken by the late reflections to vanish into silence. The higher the _Reverberance_ the longer the tail of the reverb is. The effect is especially obvious on percussive sources. The _Reverberance_ is frequency dependent and can be fine tuned by the _Heaviness_ and _Liveness_.
<br>
<br>
**Heaviness**; Relative decay time of low-frequency content, relative to the reverberance.
<br>
<br>
**Liveness**; Relative decay time of high-frequency content, relative to the reverberance.

---

## Crossover

![inline](include/SpatRevolution_UserGuide_-158.jpg)

* Crossover L - set frequency for Heaviness setting
* Crossover H - set frequency for Liveliness setting
 
^<br>
**Crossover L** Sets the frequency below which decay time is determined by the Heaviness setting, expressed in Hertz (Hz). Default value: 180 Hz.
<br>
<br>
**Crossover H** Sets the frequency above which decay time is determined by the Liveliness setting, expressed in Hertz (Hz). Default value: 5657 Hz

---

## Room Response Parameters

![inline 50%](include/SpatRevolution_UserGuide_-154.jpg)

* Early reflection min (pre-delay) and max.
* Control Early distribution and Shape.
* Cluster Min, Max, Distribution and Shape.

^ 
<br>
**Early Min** Early reflections minimum time, i.e. the time between the direct sound and the first early reflection, in milliseconds. This is the analogous of the ubiquitous “pre-delay” setting found on most reverberation processors.
<br>
<br>
**Early Max** Early reflections maximum time, i.e. the time at which these cease to appear.
<br>
<br>
**Early Distribution** Early reflections distribution. Determines the way early reflections are scattered in time, inside the Early Min. / Early Max. interval. The default setting of 0.5 corresponds to regularly spaced reflections, above these are more grouped towards the Early Max. value, and vice-versa.
<br>
<br>
**Early Shape** Governs the amplitude rise or fall of early reflections. The default setting of 0.5 corresponds to early reflections all having the same level. This mimics an acoustical space where reflective surfaces are all located at roughly the same distance to the listener. Below 0.5 early reflections decay with time, above 0.5 they rise with time. Early reflections of decreasing level would be typical of a space where most of the reflective surfaces are grouped at a range closest to the listener.
<br>
<br>
**Cluster Min**. See Early Min. ★ Please keep in mind the cluster is fed with the same input than the early reflections processor section.
<br>
<br>
**Cluster Max** See Early Max.
<br>
<br>
**Cluster Distribution** See Early Distribution.
<br>
<br>
<div style="display:none">
Comment: **!!!Need explanation about what type of acoustic spaces create this kind of asymmetric early distribution!!!**
</div>

---

## Options

![Inline 40%](include/SpatRevolution_UserGuide_-156.jpg)

* Infinite for decay time rising to infinity
* Air Absorb to simulates the frequency-dependent absorption of air
* Abs. RollOff to set the frequency for the air absorption simulation
* Modal Density for the frequency “smoothness” of the verb engine.

^
<br>
**Infinite** When activated, decay time temporarily rises to infinity, making the signal recirculate indefinitely inside the reverberation engine. This is best suited for one-off special effects such as “deep-freezing” audio material, or if you’re looking to create something a little less conventional than a fade-out for the end of your track.
<br>
<br>
**Air Absorb** Simulates the frequency-dependent absorption of air, where high frequencies rolloff quicker than low-frequencies with respect to distance. You’ve most probably noticed this real-world phenomenon when you’re far away from a concert venue and
only able to hear the bass, and gradually start to hear the whole mix as you get
closer.
<br>
<br>
**Abs. RollOff** Roll-off frequency for the air absorption simulation. Signal content above this frequency vanishes faster.
<br>
<br>
**Modal Density** Scales the modal density with respect to the current setting, which is internal to the application engine, and depends on other parameters such as reverberation time, etc. The modal density governs the frequency “smoothness” of the verb engine. Increasing this setting reduces the graininess of the reverberation. Adjust to taste, depending on the source material and desired result.

---

## Reverb Design Presets

![Inline 45%](include/SpatRevolution_UserGuide_-160.jpg)

^ <br>
The Artificial Reverberation editor has its own preset management system, where you can save pre-designed models into a user defined preset list or to disk.
<br>
<br>
This is useful for building up a collection of pre-designed reverberation spaces and for designing models that might closely match the measurements of actual spaces you already know. A list of basic presets are provided.



---

# 2.4.2 Source object parameters review 
	
^ 
<br>
Every Source in a Room has its own set of variable parameters which define its simulated positional information, psycho acoustic properties, virtual acoustic properties and other options.
<br>
<br>
To edit the variables of a source in the _Source Parameter_ editor, you must first be inside a Room. Select the source you want to edit from the list on the left side panel of the Room editor by left clicking on its Index number. Alternatively, grab its 'emitter' object in the 3D Room visualisation (or just one of them, if the source is a multichannel group). When you select a source, the _Source Parameter_ editor will pop up as a set of categorized groups with which you can alter the properties of the Virtual Source in the Room.
<br>
<div style="display:none">
Comment: [//]: #TODO  "Move to another part the following paragraph"
</div>
Additionally a _right click_ on a Source Index number will bring up some further options, especially useful is the **Colour** option, which allows you to set an identification colour to a Source or Group.

---

## Perceptual Factors

![Inline](include/SpatRevolution_UserGuide_-170.jpg)

* Comes from years of studies from IRCAM
* Control perceptive sensation instead of technical parameters
* We encourage you to learn the meaning of these parameters by carefully listening to the audible characteristics
 
 > **Some Spat Reverb parameters control how the acoustics are _perceived_**

^ 
<br>
This parameter group holds settings affecting the way the sources direct and reverberated acoustic properties are perceived by the listener.
<br>
<br>
As touched on previously, these are not simply names stuck onto a single internal parameter dictated by the inner workings of the algorithm. Instead, a true perceptually-oriented approach was used in the design, where a test panel of listeners was presented with a test-set of sounds, constructed from several different variations of the reverb engine inner parameters. The listeners were then asked to rate each set onto a few different scales with perceptually and aesthetically meaningful names. Using principal components analysis (PCA) and optimisation techniques, we then built an algorithm which reverses the process and automatically maps a given set of perceptual factor values to the many internal reverb engine parameters.
As a general guideline, we encourage you to learn the meaning of these parameters by carefully listening to the audible characteristics when adjusting them. We do provide a short explanation of each of them below, but training your ears is really the best way to be able to use these in context.
<br>
<br>
**Presence**; Source presence refers to the prominence of the direct sound with respect to the reverberated sound. It is not just equivalent to a dry/wet ratio, and is influenced by other settings such as distance, radius and drop-factor. 
<br>
<br>
**Warmth**; Presence of the low frequency content part of the source.
<br>
<br>
**Brillance**; Presence of the high frequency content part of the source.
<br>
<br>
**Room Presence**; Prominence of the reverberation tail with respect to the source, or in other words, how much the room sound dominates the overall sound.
<br>
<br>
**Running Reverberance**; This parameter controls the amount of perceived reverb when feeding a continuous music message, where the overall sound is a tight blend of the dry and wet signals and the reverb part cannot be mentally separated. It is linked to the early reflections decay time of the Spat Revolution Reverb engine. Note: this setting is not the same as the ‘reverberance’ in the _Reverb Properties_.
<br>
<br>
**Envelopment**; Envelopment corresponds to the perceived notion of how much the listener feels that they are surrounded or immersed by the ambient sound. In a multichannel configuration, one could describe this as the feeling of being wrapped inside the imaginary “sound sphere” that the listener pictures in her mind. It can also be described as the energy of the early room effect with respect to direct sound.

---

## Reverb Options

![Inline](include/SpatRevolution_UserGuide_-172.jpg)

* Control over global or various reverb stages
* Early Reflections - perception of sound source localisation.
* Cluster - The cognition of room acoustics
* Diffuse reverberations tail - size and reflectivity of an acoustic space

^ 
<br>
**_Reverb Enabled_** Toggles whether a source will use the all lever of the reverberation engine.
<br>
<br>
**Early / Cluster / Tail** Toggle whether a source will use only some or all of the different reverberation stages.
<br>
<br>
_Early_ refers to _Early Reflections_ stage of the Room response which is one of the most significant stages involved in our rapid aural perception of spatial properties and sound source localisation.
<br>
<br>
_Cluster_ refers to a secondary iteration of room response reflections and is quite significant in the cognition of room acoustics.
<br>
<br>
_Tail_ refers to the diffuse reverberations that eventually decay in a direct relationship with the size and reflectivity of an acoustic space. The tail section of a reverb does not contribute much to the localizability of a sound source in a space, but instead gives a sense of depth and ambience.

---

## Axis Omni Filters

![inline](include/SpatRevolution_UserGuide_-174.jpg)

* Equalizer designed for virtual sound emitters simulated in virtual spaces
* Spectral omni filters treat the room response of the source
* Spectral Axis filters treat the direct sound of the source

> ★ **_Spectral Axis_** **performs more like conventional mixer EQ**

^ <br>
These two spectral processors can be considered as being equalizer that have been especially designed for virtual sound emitters simulated in virtual spaces.
<br>
<br>
**Spectral Omni**; The omni directional part of a given signal is considered to be the room response of this signal. The Spectral Omni filter section allows to tailor the frequency response of the room for each sources.
<br>
<br>
**Spectral Axis**; The axis part of a given signal is considered to be the direct input of this signal. The Spectral Axis filter section allows to tailor the frequency response of the direct sound of each sources. 
<br>
<br>
★Speaking with a more usual sound engineer vocabulary, the Spectral Axis filters section allows to equalize the dry signal and the Spectral omni allows to equalize the wet signal. Setting a rather flat on-axis equalizer curve, and maybe cutting the treble and mids for the omni response would be a good starting point to emulate a real-world sources, so this is the default setting for these filters.

---

## Radiation

![inline](include/SpatRevolution_UserGuide_-176.jpg)

* Position of a source using spherical coordinate system
* Angle of a source direct orientation relative to the listener-source axis
* Aperture parameter relates to the “sound cone” projected by a source in the acoustic space

> ★ **_Pitch and Yaw_ can be used to make a source more diffuse by turning its direct sound away from the listener**

^ 
<br>
This section controls the simulation of acoustic radiation in relation to the location and emitter orientation of the virtual source. Use these parameters to simulate how a source will interact inside the reverberant environment.
<br>
<br>
**Relative Direction**; This switch is a very simple way for a user to achieve a more consistent result as regards the natural conservation of a source's presence. The algorithm will continuously maintain the on-axis focus for each virtual source - or for every emitter in a
grouped source - so that it is consistently oriented towards the listener position. When not engaged, a source remains in the same constant direction which is what might be preferred if something is passing through in a spatial design.
<br>
<br>
**Distance**; Distance from the source to the center reference point (listener position), in meters.
<br>
<br>
**Azimuth**; Angle between the source location and the listener position front reference axis, in
degrees.
<br>
<br>
**Elevation**; Elevation angle, in degrees.
<br>
<br>
**Yaw**; Angle of the source direct orientation relative to the listener-source axis, in degrees.
<br>
<br>
**Pitch**; Source direct orientation pitch angle, in degrees. Think of _pitch_ in the nautical sense of the word, how a boat _pitches_ up and down in stormy seas.
<br>
<br>
**Aperture**; The aperture parameter relates to the “sound cone” projected by the virtual source in the acoustic space, and is measured in degrees. It determines wether the source will be very directive (small aperture), or omnidirectional (large aperture) inside the reverberant environment. ★ **Aperture can make a source 'activate' more of the acoustic
space**


---

## Send LFE

![left 70%](include/SpatRevolution_UserGuide_-180.jpg)

* Send an amount of the source into the dedicated LFE
* This parameter will only be available in a Channel-Based room that include a LFE



> ★ **Automate the _LFE send_ for dynamic low frequency effects**


^ 
<br>
This variable parameter will only be available when the room is a Channel Based Format which features an LFE speaker in its configuration, such as DTU7.1 / 5.1 / AURO and ATMOS for example.
<br>
<br>
It will send an amount of the source into the dedicated LFE speaker channel of the output channel based configuration.


---

## Spreading

![inline](include/SpatRevolution_UserGuide_-178.jpg)

* Spreading is a percentage factor that defines how a sound source will appear to spread out across speakers
* Nearest Neighbours
	* Only available in KNN room
	* It sets a maximum limit to the number of speakers that the algorithm can use as neighbours

^
<br>
**Spread Factor**; Spreading is a percentage factor that defines how a sound source will appear to spread out across speakers or virtual speakers. It is similar to _Aperture_ in its focussing effect but will translate differently across certain channel based speaker arrangements according to how many speakers are involved.
<br>
<br>
**Nearest Neighbours**; This parameter is only available to a source, if the room it is simulated in has been specified to be using the _K Nearest Neighbour_ panning type (see section 5.64). It sets a maximum limit to the number of speakers that the algorithm can use as neighbours in its search for speakers to activate in relation to a virtual source. On a 10 speaker setup, 1-10 % will be the closest speaker to source. 11%-20% will be 2 and so forth.

---

## Multiple Source Selection

![inline](include/SpatRevolution_UserGuide_-166.jpg)

* Distribute the sources in the group evenly in a circle spread
* Generate different colours for the sources
* Reset the positions of the group

^
<br>
You can shift-click on the Index number of separate Sources to create an ad-hoc edit group. When you have group Sources in this way, you can perform a number of group edit actions. When you Right Click on an ad-hoc group selection a menu will pop up where you can:
<br>
<br>
When you have selected an ad-hoc group using the shift-click technique, you can then pop-up the _Source Parameter_ panel by clicking on the property panel header 'fold arrow' as shown in the screenshot below.
<br>
<br>
Any Source Parameter variables you adjust manually will assign that same setting on all selected sources in the group. A barycentre will then become practical to work from a center of mass perspective.

---

### Barycentric

![inline](include/SpatRevolution_UserGuide_-181.jpg)
![inline](include/SpatRevolution_UserGuide_-122.jpg)

* Parameters accessible to multichannel sources and multi-selection of sources
* Rotate a group cluster around the barycentre
* Scale the group cluster

^
<br>
When a Virtual Source in a Room has more than one channel in its format, it will be represented as a single source with ONE unique index. It will be visualized as a group in its assigned channel based speaker arrangement.
<br>
<br>
In the above screenshot, the red source consists of 5 channels arranged as a DTU 5.0 surround sound configuration.  A multichannel cluster can be conveniently positioned and manipulated _as a single group_ which maintains its correct internal spatial positioning relationships but moves in relation to the absolute listener position in the Room (the Dummy Head). 
<br>
<br>
The dot at the centre of each cluster, where each virtual 'channel emitter' is attached is called the 'BaryCentric' focus - In other words, a _relative_ listener position that the virtual source configuration remains focussed on.
<br>
<br>
These complex spatial positioning algorithms are computed and controlled in realtime using Spat Revolution's advanced _Barycentric_ and relative direction source parameters.  A group that may contain many elements can be transformed, scaled, moved and manipulated in complex ways, through only one set of controls. 
<br>
<br>
These rotational transformations will only work on a virtual source that consists of more than one emitter in a grouped channel based arrangement. They will also become active, when you _shift-select_ mono sources together to form an ad-hoc group or shift-select mono-sources in combination with grouped channel based sources. The 3 dimensional group rotations are calculated using a barycentre to transform a network of sound sources constrained in a group relationship.
<br>
<br>
**Rotation XYZ**; Rotate a group cluster around the XYZ axis of their common barycentric pivot
point.
<br>
<br>
**Scale**; Scale the group cluster, maintaining their barycentre and relative relationships.
<br>
<br>
**Relative Direction**; The barycentric transformations will continue to orient their on-axis energy towards the listener position, if the relative direction algorithm is enabled (see section 9.6)

---

### Options

![inline](include/SpatRevolution_UserGuide_-183.jpg)

* The Doppler effect modulate the pitch when a source is accelerating or decelerating
* Air absorption - Simulates the frequency-dependent absorption of air
* Drop Factor - determine the volume drop according to the distance
* Enable _Drop Log_ for an acoustically accurate setting
* Radius - set the radius of a sphere where the drop attenuation is not taken into account. Should be set to the distance of the closest speaker
* PanRev - allows you to modify cluster panning
* Early width - Controls the width of the sound projection lobe of the early reflections

^
<br>
Finally, there are some options available for each source.
<br>
<br>
**Doppler**; The Doppler effect is a well-known wave propagation phenomenon where the pitch of a sound perceived from a listener standpoint rises when the source is accelerating, and falls when decelerating. This is the fire siren pitch going up then down when passing you. It will only be heard if you rapidly move the sources locations quite fast, but thanks to the virtual nature of the Spat, you can bypass Physics’ laws and manually inhibit it using this switch, should it be unsuitable for the particular application you are dealing with.
<br>
<br>
**Air Absorption**; Simulates the frequency-dependent absorption of air, where high frequencies rolloff quicker than low-frequencies with respect to distance. You have most probably noticed this phenomenon when you are far away from a concert venue and only able to hear the bass, and gradually start to hear the whole mix as you get closer.
<br>
<br>
**Drop Factor and Drop Log**; Owing to a fundamental law of acoustics and geometry - namely energy conservation - sound pressure drops in level as one moves away from the source. Enable _Drop Log_ for an acoustically accurate setting, which corresponds to a drop value attenuation every time the distance from the source is doubled (logarithmic behaviour). The default _Drop Factor_ of 6db is also the acoustically accurate setting.
<br>
<br>
**Radius**; Specifies the radius of a sphere or disc in meters, cantered around the listener position, where the drop attenuation is not taken into account, and the sound level is kept constant with regards to distance. This is not only useful to prevent any dramatic sound level peak when placing a source too close to the listener, it also reflects real-world behaviour quite accurately, where sources do have a certain physical size, unlike point sources that are commonly used to model far-field acoustics.
This “no-drop” zone is displayed as a transparent sphere of matching radius in the Room graphics.
<br>
<br> 
**PanRev**; By default, only early reflections are panned, and the cluster reflections, which form the diffuse part of the early reverberation, are panned dead center. _PanRev_ allows you to modify cluster panning, thus imparting some directionality or perceived direction to the diffuse part of the sound.
<br>
<br>
**Early Width**; Controls the width of the sound projection lobe of the early reflections from a source in the virtual acoustic space, in degrees. The minimum setting, 1°, gives a very directional source, whereas 180° makes it omni-directional.

---

## Smart Property Filter

![inline](include/SpatRevolution_UserGuide_-168.jpg)

^
<br>
This features allows you to display one or several parameters for all the sources that are in the same Room. It is a useful feature for fast editing. Type "azimuth elevation distance " in the filter box for example, and you will see faders appear for only these properties, grouped for each of the sources as demonstrated in the following screenshot.

---

* Perceptual factors of sources
* Source parameters 
* Concept of Radius
* Input methods and Movement behaviours  (Polar/ Cartesian)

---

# 2.5. Hands-On exercises 

2.5.1. Configuring Spat Revolution          
2.5.2. Panning / Reverberation Control              
2.5.3  Creating custom speaker arrangements

---

## Hands-On exercises: Spatial Audio Productions

             
* [Configuring Spat Revolution](2_5_Hands_On_2_5_1.md)
* [Speaker arrangements](2_5_Hands_On_2_5_2.md)
* [Panning / Reverberation Control](2_5_Hands_On_2_5_3.md)

---
## Configuring Spat Revolution

* Typical studio productions & Live Sound scenario
* Configuring Spat Revolution with DAW template
* Transcoding to CB. Transcoding Binaural - 
* Easy Setup, Source  and Room Manipulation Shortcuts 
* (Room toggle, Source Live/Circle, Reset position, colours, all)


---

### Parallel Room Mixes

![inline](include/SpatRevolution_UserGuide_-201.jpg)

^
<br>
Use the lasso-selection or command-click selection to make a selection of all
Source modules in the Sources row of the graph. Use the Connect Action to wire
them into another Room module. This can be repeated, according to how many
alternative Room mixes are needed.
<br>
<br>
The mix and automation of all sources will be rendered identically in each room,
except of course the Room format, panning type and artificial reverberation could
all be different.
<br>
<br>
The parallel Rooms technique is used to create simultaneous versions of the
project mix at the outputs. For example a scene can be computed as a Channel
Based mix, an HOA encoded mix and a Binaural mix simultaneously.


---

### Quick Start

![inline](include/SpatRevolution_UserGuide_-205.jpg)

^
<br>
Spat will automatically wire up a suggested signal graph, adding modules in-between as needed when you choose a _Connect Selected_ Action between modules.
<br>
<br>
This is particularly useful for fast setup from scratch. Add some inputs on the top
row, add some outputs on the bottom row. Select all and choose _Connect_. A starting signal graph will be generated automatically.

---

### Disconnecting and Connecting

![inline](include/SpatRevolution_UserGuide_-203.jpg)

> ★ Try not to Remove Modules until you are certain that this is the
correct edit action.

^
<br>
As mentioned earlier on, it is recommended to use _Disconnect Selected_ type Actions before going for a _Remove Selection_. This is because the graph will automatically re-organise itself when Modules are deleted and this could be difficult to revert. It is also worth knowing that you can multi-select modules (using _CommandClick_ or _Lasso select_ ) before choosing an action, and all modules in the selection will be affected by the action.

---

### Drag and Connect

^
<br>
This feature also works on a  selection of multiple blocks of the same type. For example, if we wished to connect 5 inputs to 1 output, we can select our inputs a drag them  on the output. All the inputs blocks will be patch to a room block thru sources, and the room is patch to the output thru a master block. (With the default stereo room that can be changed later) 

---

### Drag and Drop
![inline](include/drag&drop3.gif)


^
<br>
The drag and drop  feature also allows reorganizing the blocks of the same type. This means that you can now change the order of already created blocks. This gives to the setup page a more ergonomic and flexible feel. **Important to note that this will be changing the index number of the source. So be careful with automation already created. This is specific to OSC like using the plugins with OSC where the index is important. Not the case with software sources/inputs which use a different ID system**

---

### Multi Matrix Routing

![inline](include/SpatRevolution_UserGuide_-207.jpg)


^
<br>
When working with multiple hardware inputs, group a selection using command-click or _lasso drag_ before pressing the _Show Input Matrix_ action to construct a grouped Matrix IO overview, which can provide a better understanding of the input channel routing in complex setups.

---

### Room duplication

![inline](include/SpatRevolution_duplicateRoom.gif)

---

### Room duplication

![left](include/SpatRevolution_duplicate_selected_room.png)

Spat allows to quickly duplicate a room with a few option to help the user to optimize the routing process. To access this menu, simply click on the "Duplicate Selected" button.

The new pop-up windows allows to:

* Rename the duplicated room
* Choose if the sources routed to the original room are routed the new one, or duplicated, or nothing is patched.
* Choose if the outputs of the original rooms are duplicated, mirrored or nothing is done to the duplicated room.


---


## Speaker arrangements

* Creating custom arrangements 
* Managing speaker setups


---

## Panning / Reverberation Control              

* Customizing the room reverb
* Using simultaneous rooms for various acoustics 
* Adjusting the source radius to arrangements 
* Building an object based sound scene
* Manipulating the source reverb properties
	
---

# 3. Spat Revolution Integration		
---

### 5.5Hr Module - SCRIPTING, AUTOMATIONS, INTEROPERABILITY, COMMUNICATION

* 3.1. Getting Started with integration.

* 3.2. Using Snapshots in SPAT Revolution.

* 3.3. Automation & audio sequencing with SPAT Plugs-ins.

* 3.4. OSC interaction and integration.

* 3.5. SPAT terminal and system troubleshooting.

* 3.6. Specification and Hardware recommendations

* 3.7. Hands-on exercise: (How To) (customized to class).	
---

# 3.1. Getting started with Integration

* 3.1.1.	Typical automation integrations, protocols and workflows
* 3.1.2.	What is OSC?
* 3.1.3.	Understanding the dual coordinate systems (Polar vs Cartesian


---

## 3.1.1. Typical integration: protocols, automation & workflow


---

## Automation

![inline](include/SpatRevolution_UserGuide_-185.jpg)

* Spat Revolution Send Plug-ins
* OSC message from third party controllers

> **★All parameters of Spat Revolution can be continuously controlled in realtime.**


^
<br>
Control data can be sent via _Open Sound Control_ ( **OSC** ) or through multiple SPAT plug-ins in your **DAW**.  Parameter control can be played back from pre-composed timelines, or performed, generated and captured in a variety of ways. 
<br>
<br>
One of the most straight-forward ways is to set DAW automation to Write mode on a track that contains a Spat Send plug-in, and use the graphical interface of the Spat Room Editor to drag Virtual Sources around or turn source parameter pots. 
The movements will be captured into the DAW timeline in precisely the same way you would capture automation from a conventional DAW plug-in, like [Reaper](), [Reavolution](), [ProTools](), [Nuendo](), [Ableton Live](), [Bitwig](), or other.
<br>
<br>
Alternatively, OSC control surface such as _LEMUR_ running on an iPad (wired or wireless) could be used to control the parameters of Spat in realtime whilst you stand in the middle of the sound system away from the computer. There is already various  _Lemur_ template available for Spat (see "Third party integration" - Lemur in Spat Revolution documentation)
<br>
<br>
If you are using _Figure53 Qlab_ for show control, spatial effects can be sent along with the rest of the audio visual cues for a big show or event.  ( see "Third party integration" - QLab in Spat Revolution documentation)
<br>
<br>
If you are working with algorithmic gesture generators and modulators then your
controls signals can be easily sent into the Spat Renderer via OSC to distribute and control spatial sound sources in realtime using your own control programs.


---

### Remote and interaction with Spat Revolution 

<div style="display:none">
Comment: Need image
</div>

* iPad application such as Lemur or TouchOSC
* Show controllers such as QLab, Ovation, and BrainModular Usine
* Graphical sequencer and interactive media software

> *★Spat Revolution relies intensively on OSC to provide full control over sources, rooms, reverb, snapshots and global properties.*

^
<br>
Interaction with Spat Revolution is a very important part a live concert integration. The good news is that Spat Revolution fully integrates OSC and can be deeply controlled. The list of possible OSC controllers is wide and can't be all mentioned. You just want to make sure the tool supports custom OSC grammar. 
<br>
<br>
Dedicated Lemur template are available as a good starting point to control Spat Revolution. It is possible to setup multiple iPad with multiple dedicated tasks.
<br>
<br>
QLab, Ovation, and BrainModular Usine are also excellent choices for live concerts. It can be used to trigger specific path and trajectory during the show. Spat Revolution is also compatible with real time tracking devices such like BlackTrax.
<br>
<br>
Graphical sequencer and interactive media software such as Max MSP, PD, OSCulator, IanniX.

---

![inline](include/SpatRevolution_UserGuide_-187.jpg)

> **★Get creative with spatial sound design using OSC and Spat**

<div style="display:none">
Comment: to review
Nicolas's note: I don't know why this part is here ... this doesn't correspond to the title and the part

Hugo Comment: YES. WE HAVE TO THINK WHERE THIS NEEDS TO LAND.. ISNT THIS JUST MORE FOR THE WORKFLOW SECTION???
</div>

---

### Single computer setup (LAP)

<div style="display:none">
Comment: Need image
</div>


* Three plug-ins to integrate your host and Spat:
	* Spat Send & Return for audio pipelines and automation.
	* Spat Room for automation only.

> *★You may only can or want to use a single computer*

^
<br>
Single computer configuration is great for portable system and for various creation such as live concert preparation. In such scenario you need a software  I/O method (virtual I/O) to exchange multichannel audio from and to the software running on you computer. This is not a trivial task, and many previous solutions have been prone to drop outs and other problems.
<br>
<br>
In answer to this challenge, FLUX:: have created three plugins for AU, VST and AAX hosts. The Spat Plug-ins offer a straightforward way to integrate the Spat Revolution spatialization environment with other digital audio workstation environments - _running on the same machine._

---

### Hardware Workflow


![inline](include/SpatRevolution_UserGuide_-128.jpg)

Hardware inputs connections could include:

* Mic / Line
* MADI
* AoIP: AVB / AES67 / DANTE 
* AES3
* ADAT

> *★Make sure you have the Hardware Device selected in the Spat preferences!*

^
<br>
When you want to be receiving and routing audio from an audio I/O  hardware device (physical or virtual) connected to your Spat Revolution workstation, you need to make sure this device is selected in the Spat Revolution preferences. By default manually added input and output modules are considered hardware I/O ready to be patched. They are labelled 'Hardware'.
<br>
<br>
Hardware input and output arrangement formats can be mono, stereo or multi-channel  with any number of channels. Hardware signal channels can be patched to single sources, or as a multichannel source group using only one input/output module.![](include/SpatRevolution_UserGuide_-130.jpg)

---

### Converting Software to Distributed Hardware I/O Workflow

* A network of computers.
* Hardware I/O to isolate playback and Spat processing.
* Disabling LAP activates OSC Network message I/O.

> *★Enable bi-directional OSC communication in Spat preferences to send automation over the network to other computers.*

^
<br>
Routing via hardware I/O means the audio arrives to Spat Revolution via hardware inputs ideally with a multichannel audio format such as MADI or AoIP Interfaces from another computer handling the audio playback (and/or recording) as well as the automation. This is a powerful and reliable combination as it shares computational resources.
<br>
<br>
Furthermore, a single computer configuration can be easily converted to a fully distributed system  where automation is then travelling as OSC messages targeting a single or dual Spat Revolution computer engine ideal for real time production hardware setups.



---

### Dedicated Spat Revolution computer

<div style="display:none">
Comment: Need image
</div>

* Best practice includes using a dedicated computer.
* MADI and AoIP are great for their multichannel audio support.
* Spat Plug-ins can be hosted for automation to OSC.
* Solid hardwire ethernet network preferred OSC UDP Communication.


^ 
<br>
The best way to use Spat Revolution is to dedicate a computer to it. Spatial audio processing can be really hard on CPU and best practice includes using a dedicated computer.
<br>
<br>
MADI is a great option to send audio between computers: it can easily send 32, 64, 96 and even more channels at various sample rates. AoIP  (Audio over IP) are also very good option, with Dante, AVB or AES67.
<br>
<br>
Spat plug-ins can be used to send automation thru OSC when a host is available in the system. Alternatively many consoles and show / remote controller can implement generic OSC messages.
<br>
<br>
Using OSC on a network can potentially support the use of wifi connectivity but it is recommended to use an hardwire ethernet connection between your devices. To note that OSC use UDP to send informations over the network: there is no guarantee that an emitted message will be received and wireless systems can easily drop messages here and there.

---

### Spat in AoIP with audio consoles

<div style="display:none">
Comment: Need image
</div>

* Flexibility, Simplicity
* Widely available as "native" to consoles
* Low latency with physical Dante interfaces (non DVS)

> *★In a live context, we recommend using Audio over  protocols to IP to interface console with Spat Revolution computers.*

^
<br>
In the live world, consoles are the main tool of audio mixing engineer. They are reliable and designed to be responsive. Therefore, the use Spat Revolution in a live context means interfacing with numerous mixing desk.
<br>
<br>
To do so, we need to consider the available I/O protocol of a given console and use a dedicated interface of the same protocol for Spat Revolution.
<br>
<br>
Dante, for exemple, is a very common AoIP mechanism, used by many consoles manufactures. When using Spat Revolution with Dante, a dedicated Dante interface  (USB, TB or PCIe) is the recommend scenario to ensure the lowest latency possible. Dante Virtual Soundcard (DVS) will not meet this requirement. AVB, AES67 or Ravenna are all other good options for Spat Revolution. MADI is again a great choice and is very reliable. But it does not offer the same flexibility than an audio network.

---
# 3.1.2. What is OSC?

* A UDP network-based communication protocol
* Musical performance or show control data
* Interoperable, accurate and  flexible.
* More precise and complete than MIDI

^
<br>
Open Sound Control (OSC) is a protocol for communication among computers, sound synthesizers, and other multimedia devices that is optimized for modern networking technology. Bringing the benefits of modern networking technology to the world of electronic musical instruments, OSC's advantages include interoperability, accuracy, flexibility, and enhanced organization and documentation.
<br>
<br>
This simple yet powerful protocol provides everything needed for real-time control of sound and other media processing while remaining flexible and easy to implement.
<br>
<br>
**Features:**
<br>
<br>
* Open-ended, dynamic, URL-style symbolic naming scheme
* Symbolic and high-resolution numeric argument data
* Pattern matching language to specify multiple recipients of a single message
* High resolution time tags
* "Bundles" of messages whose effects must occur simultaneously
* Query system to dynamically find out the capabilities of an OSC server and get documentation
<br>
<br>
There are dozens of implementations of OSC, including real-time sound and media processing environments, web interactivity tools, software synthesizers, a large variety programming languages, and hardware devices for sensor measurement. OSC has achieved wide use in fields including computer-based new interfaces for musical expression, wide-area and local-area networked distributed music systems, inter-process communication, and even within a single application.


---

## 3.1.3.Real-time tracking 

![inline](include/SpatRevolution_UserGuide_-341.jpg)

* OSC and RTTrPM tracking options
* Tracking data mapping to sources or listeners
* Integrates with real-time performance tracking system
* Attach listener position in a room for head-tracking

> *★Listener and Sources comes with six degrees of freedom (6DoF)*


^
<br>
Spat Revolution supports realtime tracking from OSC and RTTrPM protocol. The later is the protocol created by Cast Software and BlackTrax.
<br>
<br>
OSC tracking gets implemented like any OSC control and great tracking system for Zactrack and TTA Stagetracker to name two. 
<br>
<br>
When using BlackTrax RTTrPM tracking protocol in Spat. Preferences exist to map BlackTrax tracking beacons with Spat source objects and Spat room listeners. Listener tracking brings the ability to lock the head (head-tracking) of an individual to a binaural room listener position
<br>
<br>
With BlackTrax you assign a Beacon ID to an actual audio source object or to an actual room (listener position tracked)
<br>
<br>
More specific information can be found on the BlackTrax Real-time Tracking Appendix.

---

###  Listener position 

#### In the actual room output parameters in the room view, you actually see listener positon and have the ability a scale the tracking data

![left](include/SpatRevolution_UserGuide_ListenerPosition_Tracking.png 'size=350x')

---

# 3.2. Using Snapshots

* 3.2.1. Creating snapshots
* 3.2.2. Recalling snapshot with interpolation timing 
* 3.2.3. Managing snapshots

![inline](include/Sync.png)

^
<br>
Snapshots are an important part of a live show. It can be used to capture an audio scene into Spat Revolution. Sources, rooms and masters properties are stored in a snapshot. It allows a complete transformation of the soundscape, with interpolation. 
<br>
<br>
Be careful: To use snapshots, timecode need to run in Spat Revolution. Two ways to run the Timecode:
<br>
<br>
- if working with Hardware IO, an audio device must be selected into Spat preferences.
<br>
<br>
- if working with Local Audio Path, the DAW needs to play back and the Spat session needs at least one send and one return connected together.
- <br>
The timecode activity is apparent in the bottom left of the screen. If timecode isn't running, recalls with interpolation time will fail.
 
---
### Snapshot Menu

The snapshots can be controlled with the dedicated menu, or with OSC messages.

![left](include/Snapshot_menu.png)

![right](include/SpatRevolution_snapshot_recall.gif)

---
 
## 3.2.1. Creating snapshots from menu

[.hide-footer]

^
<br>
We can create a snapshot:
- by using the "Create" action into the "Snapshots" menu.. In this case, the snapshot will be added at the end of the list. The shortcut <code>Alt + Space</code> could also be used to capture a snapshot.
<br>
<br>
- by using the "Insert Before" action.  This option is available only if another snapshot exists. 
The snapshot will be insert before the selected snapshot, and all the snapshots will be renumber.
<br>
<br>
- by using the "Insert After" action. This option is available only if another snapshot exists.
The snapshot will be insert after the selected snapshot, and all the snapshots will be renumber.

---

## 3.2.2. Recalling snapshot with interpolation

[.hide-footer]

^
<br>
Recalling a snapshot will recall all the current stored properties of the snapshot and with interpolation recall time if set. Different options could alter the snapshot running;
<br>
- Recall time. This option is available in the menu "Snapshots/Options recall". The values are range between 0 and 3600 seconds.
<br>
<br>
- Recall Sources / Room / Master. As all the properties are stored into snapshots, this options give us the possibility to enable or disable the recall of some properties. (recall safe)
The recall of each section could be separately activated. !> Be careful with the Room properties recall: changing some properties like Reverberation Density or Size causes reverb reconstruction (and audio drops).

---

## 3.2.3. Managing snapshots

[.hide-footer]

Different management actions can be executed with snapshots:
 
 - updating a snapshot
 
 - renaming a snapshot
 
 - removing a snapshot
 
 - remove all snapshots

 ---
 
### Managing snapshots with OSC
 

Different actions are available for handling snapshot with OSC messages:

- Create a snapshot: <code>/snapshot/create</code>. 
- Recall a snapshot: <code>/snapshot/recall.
- Update a snapshot: <code>/snapshot/update [index]</code>
- List all the snapshots: <code>/snapshot/list</code>
- Len the number of snapshots: <code>/snapshot/len</code>
- Rename the snapshot: <code>/snapshot/rename [index, name]</code>
- Remove a snapshot: <code>/snapshot/remove [index]</code>

^
<br>
- Create a snapshot: <code>/snapshot/create</code>. The snapshot name could be added in argument.
<br>
<br>
- Recall a snapshot: <code>/snapshot/recall [index, *time, *Recall Effective Selection, *Recall Actual Selection] </code>
<br>
 _Index_: the snapshot index to recall. It can be replaced by the snapshot name.
<br>
 _Time_: optional, it will define the recall time. If not given, the default value is 0s.
<br> 
 _Recall Effective Selection_: optional, if the value is <code>True</code>, the sources' selection on the snapshot creation will be recalled. It's the default value. If <code>False</code>, selection will not be recalled.
<br>
 _Recall Actual Selection_: optional, if the value is <code>True</code>, only the parameters of selected sources' will be recalled. Else, all the sources will recalled (default behaviour).
 <br> 
<br>
- Update a snapshot: <code>/snapshot/update [index]</code>
_Index_: the snapshot index to update. It can be replaced by the snapshot name.
<br>
<br>
- List all the snapshots: <code>/snapshot/list</code>
This will return the list of the snapshot, index and name.
<br>
<br>
- Len the number of snapshots: <code>/snapshot/len</code>
This will return the total number of snapshots.
<br>
<br>
- Rename the snapshot: <code>/snapshot/rename [index, name]</code>
_Index_: the snapshot index to rename.
_Name_: the new name of the snapshot.
<br>
<br>
- Remove a snapshot: <code>/snapshot/remove [index]</code>
_Index_: the snapshot index to remove. 
It can be replaced by the snapshot name.
!> Be careful using it: there isn't any confirmation. 
 
 ---

# 3.3. DAW Integration for automation & sequencing

<div style="display:none">
WRITING NOTE: Do we want to detail operation for several daw? Maybe this section could be rename "DAW Integration" and we could present templates and detail operation with links to our videos.

COMMENT: THIS SECTION IS TO BE GENERIC INSTRUCTIONS TO DAW INTEGRATION. SO IT SHOULD BE LIGHT. YES EACH OF OUR APPENDIX DAW SPECIFIC WILL COVER. NAME CHANGE DONE AND CONTENT CORRECTED.

Section 3.3(3,4,5) will be light
 
</div>

* 3.3.1. Using SPAT Plugin as an audio pipe and for automation
* 3.3.2. Understanding DAW audio routing 
* 3.3.3. Writing automation to timeline
* 3.3.4. Editing automation
* 3.3.5. Mapping parameters to control surfaces 

---

## 3.3.1. Using SPAT Plugin as an audio pipe and for automation

![inline](include/SpatRevolution_UserGuide_-132.jpg)

> *★Spat Revolution comes up with three plug-ins: Send, Return and Room. Spat Send & Spat Return are audio pipeline which allow to send audio to Spat and return it to a DAW. This feature is called LAP  "Local Audio Path".*

^
<br>
Each instances of Spat Send and Spat Return is to be considered as a virtual cable, either going from the DAW to Spat or from Spat to Reaper. Along with the "Spat Room", these three plug-in carry automation information thru this virtual cable.
<br>
<br>
This feature is called "Local Audio Path" and can be activated by clicking on "Enable" on the bottom left part of the user interface of Send and Return plug-ins.
<br>
<br>
The following setting are possible in the Spat Plug-ins: 
<br>
**Index** - Relates the Plug in automation to a Virtual Source- INDEX is assigned automatically and can only be changed manually to an Index number that is not yet in use by another Spat Plug In instances.
<br>
<br>
**Local audio path** - Enable LAP, the inter-application audio pipe.
<br>
<br>
**Thru** - In Send only, choose if you do not want to mute the send audio through the plugin
<br>
<br>
**OSC Second Output** - Set up a second parallel OSC destination
<br>
<br>
**Report Latency** - Activate latency compensation reporting for the DAW
<br>
<br>
**Override** - In Return only, override the DAW input path
<br>
<br>
Appendix section of this guide provide DAW specific instructions a with start templates. Furthermore A Youtube playlist with a collection of video about how to setup DAWs with Spat Revolution is disponible [here](https://www.youtube.com/playlist?list=PL_Dcg2GwhLHkk4JUNIwGnHLFC5-XFlCHG).

---

### Spat Send Plugin


* Send multichannel audio from a track to Spat input module.
* Provides DAW automation of all Source related parameters
* Index# is generated automatically and refers to Spat Source

---

### Spat Return Plugin



* Returns multichannel audio from Spat output module to a track.
* Enable OSC communication for Return parameters.
* Index selects which Master to Automate


---
### Spat Room Plugin


* Enables DAW automation of all Room related parameters.
* OSC communication for Room parameters.
* Index# selects which  Room# to Automate.

---

## Spat Integration

> *In order for the audio software integration to function correctly, the user needs to take into account certain principles of routing and config*
<br>

* Sample Rate must match in both Spat and and the Plug-in Host.

* Buffer Size must match in both Spat and the Plug-in Host.
 
^
<br>
You can configure these settings in the Spat Revolution Preferences, and matching settings also needs to be configured in the host DAW Preferences. Additionally, there is an IO configuration setting inside each plug-in, accessible from the small 'cogs' icon.

---

![inline 40%](include/SpatRevolution_UserGuide_-134.jpg)

*Set the channel count Config. for each of the plug-ins instances. They each can carry up to 64 channels to and from Spat. Once done, _Enable_ the software routing using the _Local audio path_ switch*


---


> *★On some machines, you need to use the TAB key to register a new Track
Name or IP address change in a Spat Plug in*
<br>
<br>
<br>

![inline](include/SpatRevolution_UserGuide_-136.jpg)


^ 
<br>
If Spat is running, a SEND or RETURN I/O module will automatically appear in the _Environment Setup_ labelled with the _Track Name_ of the Spat plug-in, and set to the channel count you have configured in the plug-in or that you inherit for the track count. When a successful local audio stream has been established, the Send and Return modules will have a small green indicator.
<br>
<br>
The bottom status bar will as well confirm you are in sync.

---

## 3.3.2. DAW audio routing 

Sharing audio between softwares may seems straight forward but the reality is that are a lot of thing happening under the hood of a DAW that you may not be aware of. 

---

## Behind the hood

* Ensuring that Spat Send are processed before each Spat Return.
* Prevent DAW to call for audio samples that do not exist yet.
* Forcing DAW to priorize Spat Send before return with routing.

> *Each track containing a Spat Send plug-in **have to** be routed to **every and each** track containing a Spat Return plugin.*

^
<br>
It is common to say that computer can only process one thing at a time. Nowadays, we should say that one core of our CPU can only process one thing at a time. This mean that, when you are working on mix session of several dozen of tracks, the computer is actually "jumping" from one track to another to give an impression of multitask. This is, of course, overly simplified but will help you to understand what comes next.
<br>
<br>
Let's say we have a session consisting of two tracks: a track A and a track B. Both are directly routed to some output of an audio interface. The computer will not prioritize any track of the two track and process them both by "jumping" from one to another. Now, if we route track A to track B, the signal flow create a prioritization: track A must be process before the track B.
<br>
<br>
You may wonder what's the point with Spat Revolution. It turned out that Spat Send and Spat Return with both plugins that are slaved from this kind of DAW prioritization. Let's look back to our first example: we have a track A with a Spat Send and a track B with a Spat Return both directly routed to some output. Meanwhile, Spat Revolution receive audio from track A and then send back a stream to track B. In this set-up, there is no prioritization and so, track B could be process **before** track A. This mean the DAW could call for audio samples from Spat Revolution that do not exist because they were not sending by track.
<br>
<br>
This lead us to golden rule number one when working with Spat Revolution plugin : each track containing a Spat Send plug-in **have to** be routed to **every and each** track containing a Spat Return plugin. This way, we are absolutely sure every Spat Send plug-in are processed before each Spat Return plug-in.

---

* De-activate FX anticipation on Spat PI tracks

_

> *DAW Audio processing optimisation.*


^
<br>
Some DAWs use some technique to reduce the load of VST plug-ins on the CPU. One common trick is to process an audio track ahead of time and then delay the buffer to play it back at the intended moment. It is called anticipative processing. This is often very efficient and can drastically reduce the CPU load (up to 30-50% !).
<br>
<br>
The problem is that this kind of feature is not compatible with Spat Revolution plug-ins as it can break the sync between the different instances and Spat Revolution itself. Is it a big deal to de-activate prevent anticipative FX ? Not really. Either the DAW you are using doesn't use this kind of optimisation and if it does it is most likely a per-track activation.

---

### Practical routing exemples

Four recommended practices with DAW routing are available :

* Return on master track
* Single RETURN on an AUX track
* Several RETURN on AUX tracks
* Independent Dry and Wet Signals

> *★In the current version 20.12, the mixing of HARDWARE and SOFTWARE inputs is not officially supported and may report a sync loss, as Spat Revolution cannot guarantee correct sync in this scenario. Proceed with caution if this is unavoidable.*

^
<br>
To work properly, the SEND plug-ins instances must be processed by the DAW **before** the RETURN plug-in instances. To force the DAW to process this way, each track with SEND plug-in inserted must be routed (directly or indirectly) to the tracks hosting a RETURN plugin, using DAW internal routing.
<br>
<br>
Following are 4 examples of recommended practice with DAW routing, which should cover the main use cases. If your problems persist even after implementing these suggestions, don't hesitate to drop us a line at FLUX:: support.
<br>
<br>
> **PLEASE NOTE:** _In the current version 20.12, the mixing of HARDWARE inputs and LOCAL AUDIO PATH Send inputs may report a sync loss, as Spat Revolution cannot guarantee correct sync in this scenario. Proceed with caution if this is unavoidable. This is not officially supported_



---

### Spat RETURN plugin on master track

![inline](include/SpatRevolution_ReturntoMaster_1.png)

In simple projects, when having a single return plugin on a master track, you should not encounter any sync issue as long as each SEND track is routed to the master.


---

### Single RETURN on an AUX track

![inline](include/SpatRevolution_ReturntoAux_1.png)

Issues may happen when return is inserted on an AUX track. Make sure that each SEND track is routed to the AUX track (RETURN track). Here is an example using AUX send (see example below).

> *★You might achieve the same by routing the track outputs to a bus.*

<div style="display:none">
Comment: Schema to update, without the Audio routed to the master.
</div>

---

### Several RETURN on AUX tracks

![inline](include/SpatRevolution_ReturntoSeveralAux_1.png)

When several RETURN tracks are needed (for example several rooms to render from Spat Revolution, and/or several output stream formats), you will have to route each SEND track to each RETURN track, using the same technique.

^
<br>
As it can quickly become complicated as the project grows, in the following example, the use of a 'dummy' track, avoids using several AUX sends on the 'SEND 'tracks. 'SEND 'tracks. It makes routing clearer and easier to implement on larger projects. The 'dummy' AUX track is routed to all the RETURN tracks (using AUX sends or patching the output to a multichannel/multi-format 'dummy' bus).

<br>
Then, simply route all your SEND tracks to this 'dummy' track by simply patching it's output to the multichannel/multi-format 'dummy' bus or via the use via an aux send)

<div style="display:none">
Comment: Schema to update, without the Audio routed to the master.
</div>

---

### Using specific tracks as your Spat source/object

![inline](include/SpatRevolution_Independant_Dry_Wet.png)

> *★Some alternatives to keep both the dry (session) signal and the Spat Revolution return signal.*

^
<br>
One of the good practice to deal with these sources/objects you are sending for external rendering is to use tracks as objects. (similar to many object-based mixing workflows proposed by DAW). This way you can leave the session audio tracks and their channel insertion as they  are and simply send your audio track to the Spat SEND object track. This allows you to send a single audio track or multiple ones (stem) to the Spat SEND object track.
<br>
<br>
Doing this can segment your external rendering routing and is highly recommended to prevent audio track delay compensation systems in DAW to come and jeopardize the audio synchronisation between the DAW and Spat. This as well ensures that your audio track automation on levels for example is respected as some DAW don't have post-fader insertion (a pre-fader insert with Spat SEND PI will send audio to Spat Revolution prior to your fader automation.
<br>
<br>
The above best practice ensures as well that you keep both the dry signal and the Spat RETURN signals independent (when the mix requires to switch easily from one to the other), add one object AUX track per audio track to be sent to Spat, and insert the SEND plugins on these object AUX tracks. 
<br>
<br>
This way, you keep the dry signal on the audio track's output.

---

### Post fader send 

<div style="display:none">
Comment: Need diagram
</div>

> *★As very little DAW support post fader send on insert, in order to keep your track volume automation possible, the use of aux tracks for each Spat Send will provide this. Ultimately creating some objects aux tracks that represent you source in Spat Revolution.*

^
<br>
As Spat send plug-in are "virtual cable", it seems natural to "plug" them at the very end our tracks. Sadly, very few DAW support post fader VST insert: Nuendo, Sequoia and Ardour. If you wish to use Spat send plug-in in post fader, you'll need to create auxes for each track you want to send to Spat and insert the plug-in on the auxes.

---

# 3.3.3. Writing automation to timeline

[.hide-footer]


---

## DAW Automation - Local Audio Path 

![inline](include/SpatRevolution_UserGuide_-189.jpg)

> _Spat ROOM Plug-in automation requires manual OSC set up_

^
<br>
Whenever a Spat SEND plug-in is initiated in your DAW and you have enabled the
local audio path workflow (see section 3.3.1) the plug-in automatically establishes a parameter control connection with the current Spat Revolution project. You can then automate every parameter available via the Spat plug-in from your DAW automation lanes, with no further configuration.
<br>
<br>
In the above screenshot, you see the _Reaper_ DAW display all available automation parameters in a Spat SEND plug-in. Just arm and record or manually create automation lanes for the parameters you want to automate.

---

### DAW Automation - OSC

![inline 25%](include/SpatRevolution_UserGuide_-191.png)

<div style="display:none">
Comment: Image has to be updated with the new matrix
</div>

> *The first step is to go to the _Spat Preferences_ and _Enable OSC_.*

^
<br>
When you are not using the local audio path workflow, and instead working directly with a connected hardware interface, then you must setup automation manually.

---

![inline](include/SpatRevolution_UserGuide_-193.jpg)


> *★All SEND plug-in instances will have the same IP in the DAW but different and unique Index numbers.*

^
<br>
You then need to set up an OSC port and host route, in order to connect with Spat plug-ins via OSC. The port and host should match that of the Spat plug-ins. 
<br>
<br>
If you are running Spat and the DAW software on the same machine, then the IP address is always the so called _LocalHost_ (127.0.0.1) - the port must be the same as in the Spat Plug-ins. Remember that the index number of each Spat plug in links it to a source with the same index. In the case of a Spat Room plugin - it is used to identify which Room you wish to control.

---

# 3.3.4. Editing automation

[.hide-footer]

---

## Automation mode


![left 130%](include/spat_isolate.jpg)

1. You can record only the wanted coordinate
2. You can de-activate the playback of the automation line in the DAW
3. Or, you can isolate one system of coordinate in Spat Revolution.


^
<br>
When automation is recorded to a timeline, we often like to smooth out some imperfection? We also sometime simply create automation directly via editing in our DAW. This process is obviously very dependent on the DAW we are using, but, there is a few things we can talk about before going into deep DAW integration.
<br>
<br>
One important thing to understand is that Spat Revolution both work in spherical or cartesian coordinate. It is a powerful feature that allow Spat Revolution to be very versatile. But, when dealing with automation, we have to be careful to not use both coordinate system at the same time.
<br>
<br>
When using LAP, both AED and XYZ coordinate information is sent to the DAW. It is then important to only playback one coordinate system, other less, the movement will be misread. There is different option to do so.
<br>
<br>
To do so, right click on the position or radiation knob in Spat Revolution, select automation in the drop-down menu and then choose isolate. These properties will no more be affected by any automation messages.
<br>
<br>
If you are using OSC, you can select which coordinate system you are sending via the OSC matrix in the preference page. You can check the [OSC Connections Matrix](/3_4_OSC_Interaction_And_Integration_3_4_1) for more information.

---

# 3.3.5. Mapping parameters to control surfaces 

All the parameters of Spat Revolution plug-in can be mapped to a control surface. The process vary from DAW to DAW: Pro Tools rely on EUCON and their proprietary surface control, for which we have built dedicated table. Most of the other DAW use MIDI to allow plug-in remote, like Ableton, Logic and Cubase to name a few. Lastly, some DAW support OSC, such as Reaper, to map properties: this can be really useful when using such app as Lemur or TouchOSC.

---

# 3.4 OSC interaction and integration

* 3.4.1. 	OSC Connections Matrix
* 3.4.2. 	OSC Message structure and coordinate systems
* 3.4.3. 	Using OSC for Real-Time tracking
* 3.4.4.	Audio Definition Model  ADM OSC


---

# 3.4.1. OSC Connections Matrix

[.hide-footer]

---

### Enabling OSC in Spat Revolution

![right 40%](include/SpatRevolution_Enable_OSC.png)

> *In the _Preferences_ _OSC Main_ section you can enable OSC. Without this explicit checkbox, OSC traffic won't flow*

^
<br>
The _Export Parameters_ option exports a detailed description of the OSC grammar to a text file for reference. You can as well Enable _Commands log_ to log the OSC traffic for troubleshooting. More on this in the troubleshooting section.
<br>
The output rate allows changing how fast the engine react to OSC messages. The lower the value is, the more reactive Spat will be, but it will also increased the stress on the CPU. If you experienced some CPU overload when moving sources through OSC command you can try to increased the value. By default it is set to 5.0 ms.

---

### OSC Connections Matrix
#### There is a lot of flexibility in the OSC connection menu. You find it in the Spat Preferences page. 

<div style="display:none">
IMAGE TO BE UPDATED WITH SR 2020.
</div>

![left 100%](include/SpatRevolution_UserGuide_-195.png)


* Choose the input network interface and port#.
* Choose the output OSC message destination address and port#.
* Choosing the desired filter options

^
<br>
Eight different connections can be setup, either as input or output connection. It is displayed as a table where each connection is a line. The first parameter is the connection type, which offer many preset for both input and output. This preset comes with a dedicated network port.
<br>
<br>
The Matrix pull down menus identify a specified IP and Port to be either an **In** receiving data into Spat or an **Out** destination where Spat will unicast or broadcast control messages generated from any activity on paramaters (user interactions with parameter dials and source positional data or external controls).

---

### OSC Preset

OSC preset are :

- Spat plugins
- ADM-OSC
- Lemur
- Avid S6L
- Digico

^
<br>
Then the IP address need to be set. If the OSC connection is established locally, on the same computer, the port 127.0.0.1 is dedicated to local network usage. For other configuration, we need to inform the IP of the targeted device. Lastly, the port number can be adjusted to a free one. If a "custom" preset is loaded, we most likely need to edit this parameter to establish a network connection.

---

### OSC Transform


![inle](include/SpatRevolution_OSC_Input_Transform2.png)

[.hide-footer]

---

### OSC Transform

![left](include/SpatRevolution_OSC_Input_Transform.png)

^
<br>
Interfacing different devices and softwares in OSC can be problematic as each piece of equipment can have its own scale of value. To overcome these difficulties some OSC transform presets and a custom OSC transform menu has been implemented.
<br>
Transform presets are accessible for each OSC connection and allow some quick rescaling of the values.
<br>
If the included transform preset does not fit our needs, you can click on the "+" button to open the custom OSC transform menu. In this menu we can choose how to scale our input our output values. We can also choose to exclude specific OSC command from the scaling rules.



---


### OSC filter options

On OSC Output, various OSC connections options are available to configure a custom OSC output.

> *★If none of "AED packing" and "XYZ packing" are checked position command (A, E, D, X, Y, Z) are sent independently*

^
<br>
* _AED_ or/and _XYZ packing_ can be forced on output.
* _Auto-Bundle_ feature of OSC can be enabled or disabled. 
* Message can be sent with _Index as Arg_  rather then in the message (aka /source/aed, [1, 45, 45, 2] instead of <code>/source/1/aed</code>, [45, 45, 2] )
* _Ping-pong_ feature will force send messages coming from an OSC source back to it (by default, we send all message incoming to all output destination except destination that are the source of the message. The destination which is defined as the source are the output with same IP address and a port number in the range of [input OSC port / input OSC port +10]. Example : for Input <code>127.0.0.1</code> Port <code>8000</code>, Output <code>127.0.0.1</code> Port <code>8009</code> is considered as the same device, Port <code>8011</code> as another device)
* _Touch/Release_ messages are used to nicely integrate with DAW Automation features, this can de disabled on output if required or if messages are not supported by destination
* Alternatively, _ADM OSC_ grammar can be used on output rather the standard FLUX:: OSC grammar



---

## Send Object Index as Argument

<br>
<br>
e.g.  cmd : "/source/1/x 0.5" => "/source/x 1 0.5"


---

# 3.4.2. OSC Message structure and coordinate systems

[.hide-footer]

---

## OSC Grammar

FLUX:: Spat Revolution supports by default 3 input grammars: FLUX:: OSC grammar, ADM-OSC grammar and IRCAM ADMix positional grammar.								
For position / radiation messages such as XYZ and AED, it supports individual messages, abbreviated individual messages, packed messages (XYZ or AED) or partially packed messages (XY or AE or AD).

---

## OSC Table

An OSC table with all the messages has been build. The complete document can be download here: [OSC Commands for Spat Revolution](https://public.3.basecamp.com/p/fWnQ9D3R2indGgBfHiL2QZZT)

---


## Basic Form

In general, Spat OSC patterns have the form of 

<code>/source/[index]/x</code>

where [index] represents the Index of the Virtual Source or Room you wish to control with the message.



^
<br>
Is it important to understand that Spat Revolution offers both polar and cartesian method of moving a source. The three positional formats can be packed into one message if that option is set in the OSC Connections Matrix;
<br>
<br>
<code>/source/[index]/xyz</code> _Cartesian co-ordinates in meters_
<br>
<br>
or
<br>
<br>
<code>/source/[index]/aed</code> _Polar co-ordinates (azimuth, distance and elevation)_
<br>
<br>
!> Take care to automate EITHER Cartesian OR Polar not both

In cartesian, X is the left/right axis where Y is the front/rear axis. The Z is our Height. The together form the XYZ position.
<br>
<br>
In Polar, A is our Azimuth degree (+ or - 180 degree), E is our Elevation (+ or - 90 degree) , and D is our distance in Meters.


---


### Index as argument

<code>/source/xyz ifff</code>
<br>
<br>
★ where <code>i</code> is an integer denoting the index of the target, and <code>f</code> according to convention is a float denoting the values of the message.


^
<br>
Sometimes, it is more convenient to have the [index] parameter as an argument of the OSC message. This option is available in the OSC Connections Matrix, namely Index as Arg. If this option is switched in, then the messages will be of the pattern;
<br>
<br>
For more details about the Spat OSC dictionary...
<br>
<br>
If you are developing your own control systems to integrate with Spat, you might find it useful to know that it is possible to export a detailed description of all OSC patterns, syntax and usage to a text file for reference. You will find that option in the Spat preferences.
<br>
<br>
★ Enable commands log to confirm you are receiving data (Shift + F7 will open the log window)

---

### Coordinate System

![](Include/Polar_vs_Cartesian.mp4)

---

# 3.4.3. Using OSC for Real-Time tracking

[.hide-footer]

---

# 3.4.4. Audio Definition Model ADM OSC

### Software tools for object-based audio production using the audio definition mode


Object-based audio production and  workflow 

Support for ADM

As of service release SR2020, Spat Revolution supports two new OSC messaging system. 

* OSC data format (/track) from ADM players (ex: IRCAM ADMix)

* AMD-OSC format for Live Production profile

^
<br>
The Audio Definition Model (ADM – ITU-R. Recommendation BS.2076, EBU Tech 3364) is a metadata model that allows the format and content of audio files to be reliably described. Among other parameters, it allows to specify locations and individual gain values of sound sources
<br>
<br>
The ADMix tool suite was developed for experimenting with general ADM recording, playback and rendering. These tools currently only support a subset of the ADM specifications, but the most common features are already available. The tools are compatible with the Open Sound Control (OSC) protocol, which can be used to remote-control and integrate with Spat Revolution application and Digital audio workstation

---

### OSC data from ADMix player

Spat Revolution is capable of interpreting the OSC data (although with a different syntax the it's native one)  extracted from the object (location, gain value, etc) information contained in the ADM.

![inline](include/SpatRevolution_UserGuide_ADMix_Player.png)

^
<br>
Setting the OSC section of the ADMix Player is the key to this. Set the Destination Host address (127.0.0.1) if Spat Revolution is on the same computer as the ADMix player. Engage the send button (in yellow) and set the port number to the corresponding port number in Spat Revolution input)

--

### Object-based audio production - Workflow example

[.hide-footer]


--

### ADM-OSC format

ADM-OSC uses OSC for dynamic object metadata of the ADM format.

* A industry initiative to propose a standard OSC grammar
* Live Production workflow 
* Object List (Common Naming and Exclusive object info)
 

^
<br>
ADM-OSC is an industry initiative developed by **FLUX:: Immersive**, L’acoustics and Radio France (the later leading the case study and specific application) to facilitate the sharing of audio objects metadata between a live ecosystem and a broadcast or studio ecosystem. If tries to define a basic layer of interoperability between Object Editors and Object renderers in a live production workflow.
<br>
<br>
 It does so with [OSC ](http://opensoundcontrol.org/introduction-osc) a communication protocol widely used in the live industry. At the base the ADM-OSC is a specific grammar & definition. 
Immersive audio is gaining ground in different industries, from music streaming to gaming, from live sound to broadcast. [ADM ](https://adm.ebu.io/)or Audio Definition Model, is becoming a popular standard metadata model in some of these industries, with serialADM used in broadcast or ADM xml files used in the studio.
<br>
<br>
A first implementation of ADM-OSC is now included with the latest release of Spat Revolution. Other industry peers have implemented early versions of ADM-OSC such as L'acoustics (L-ISA), Merging Technologies (Ovation, Pyramix) and Yamaha Steinberg Media (Nuendo). It is supported by default on OSC input and as an option on OSC output

---

### ADM-OSC specification

![left](include/adm_osc_2.png )

The specification calls for: 

* Linear 0.00,1.00 for Gain and LFE (Aux send) message
* Invert Azimuth to clockwise
* Distance normalized to 0.00,1.00
* XYZ to a normalized cube -1.00,+1.00 (square in 2D, XY)

^
<br>
Spat Revolution supports **ADM-OSC** in input as an alternate grammar or on output as an option. The specification calls for normalized (linear) data value to provide interoperability and tend to align with the ADM protocol. Typically object-based mixing renderers will handle the scaling based on the system configuration. 
<br>



---

### ADM-OSC in Spat Revolution

![L-ISA](include/adm_osc_3.png )

^
<br>
To configure ADM-OSC, make sure OSC is enable and go to the OSC Connection section in the software preferences.
<br>
<br>
Choose an **input|ADM** preset to receive ADM-OSC data and select the receiving network interface.
<br>
<br>
Choose an **output | ADM XYZ (or AED)** preset to send ADM-OSC data. Enter the IP address of the destination. 

---

### ADM-OSC Presets

![inline](include/adm_osc_4.png)

[.hide-footer]

---

### ADM-OSC Input Presets

![inline](include/adm_osc_4.png)

^
<br>
On the OSC input connection, you can see that Port #9000 is our default incoming port and that and ADM Transformation preset is applied to match the specification. To modify the incoming range (the automation zone), simply enter your desired value. In this example, we are scaling to -3.00, 3.00.

---

### ADM-OSC Output Presets


![inline](include/adm_osc_5.png)

^
<br>
On the OSC output connection, you can see that Port #9001 is our default sending port and that and ADM Transformation preset is applied to match the specification. To modify the incoming range (the automation zone), simply enter your desired value. In this example, we are sending data form the -3.00, 3.00 zone. All output options are already set with the preset.


---


### ADM-OSC Third party example

![inline](include/adm_osc_1.png )

^
<br>
Recently, L’acoustics released their new L-ISA controller that can now output ADM-OSC as an alternate method (hardware required) and is functional to be received by Spat Revolution for example. OSC messages can be sent using the ADM-OSC format and be interpreted identically by any ADM-OSC compatible device.

---

### ADM-OSC Third party example


Furthermore, Nuendo V11 adds the support of External OSC renderers mapping bidirectionally the Multi-panner.
 
![right](include/nuendo_adm_2.png)


---

# 3.5 SPAT terminal and system troubleshooting

* Using terminal for command log 	
* Get and Send  object  properties  Flush all connections
* Cleaning Shared Memory  -Rebuilding GUI
* Deleting with Pref files / Pref issues.

---

# 3.5.1 SPAT terminal and system troubleshooting

[.hide-footer]

---

## Terminal

A menu with access to terminal is available by right-clicking in the top bar of Spat Revolution

![inline](include/SpatRevolution_UserGuide_TopBar.png)


![inline](include/SpatRevolution_UserGuide_S6L_ShiftF7_MiniTerminal.png)

Terminal can be presented various ways:

* Mini Terminal (Shift + F7) ideal for overlaying on part of your Spat screen
* Full Terminal overlay (F7)
* As a pop up window (Command + F7) 


----

### Confirming OSC Communication 

One practical way to use the terminal is to confirm the OSC traffic  and the actual received and sent messages.

In the preference page, make sure to check "Enable commands logs" option in order to view OSC communication  in the terminal. 

![inline](include/SpatRevolution_UserGuide_OSCEnable_CommandsLog.png)


^
<br>
Pressing Shift + F7 for example will give you a mini log window to see if the traffic is flowing. It is not recommended to leave commands logs enabled past the confirmation testing step. This will ensure that you don’t take up resources.

---

## Sync Issues with LAP

When using Local Audio Path (LAP), sync issues can be identified when sync indicators in Spat Revolution (bottom left corner) turns to red.  This can in some cases results in clicks, noises, and or loss of sound.

![Sync Error](include/Sync_Error_1.png)

***All 'green' indicators mean the sync is correct.***

![Synk OK](include/Sync.png)

^
<br>
Thanks to the template provided this should not happen unless the required routing is not in place (session modified, routing unpatched).  To work properly, the Spat send plugins instances must be processed by the DAW before the return plugin instances. 
<br>
<br>
To force the DAW to process this way, each track with send plugin inserted must be routed (directly or indirectly) to the 'return' tracks, using DAW internal routing (dummy busses in ProTools, direct routing in Reaper)
<br>
<br>
> CPU performance overloading could generate some sync errors. If you see red indicators on the bottom left corner section of Spat, this could be related to having a mismatch in Frame size or sample rate between the DAW and the Spat Revolution. 

---

### Frame size

If you are experiencing lost sync when using Local Audio:

* Increase the block size in the Spat preferences
* Save your project and Quit Spat Revolution
* Change the block size in your host DAW to match the new setting
* Reopen Spat Revolution

^
<br>
Frame size (sometimes called Buffer Size or Block Size) should be matched in the host DAW and Spat Revolution. A red message would identify a different frame rate the host DAW. Simply double-clicking on **smp/f** message in error will automatically change you spat block size setup to match the incoming audio.
<br>
<br>
If the audio processing is too demanding for your computer at the current block size and sample rate, you may also experience dropouts and sync problems due to CPU overload. Also please sure to read carefully the detailed advice of the various DAW in the Spat Revolution user documentation.


---

### Performance preferences

There are also some performance preferences that may help in the case that your host machine CPU is overloading and causing audio glitches.

* Lower UI frame rates
* Turn the 'Nebula Alpha' to 0 in your Rooms 
* Lowering Reverb Density to 8x8 for all Rooms
* Lower the automation rate via the engine preference
* Adjust the Multi-Core Parallel Computation Algorithm via the engine preference.

^
<br>
To lower UI graphic frame rates, go to the Spat preferences.  Changing the Edit Frame Rate will reduce pressure on the graphics updates and important when a host machine does not have dedicated GPU and CPU resource issues.
<br>
<br>
If you are still experiencing performance and sync issues, you may want to ensure that your hardware configuration meets the requirement. Consider as well to kill as many processes not required as possible (Wi-Fi/internet, background services and activity)

---

## Engine Parallel Processing profile

![inline](include/engine_profile_1.png)

^
<br>
Spat Revolution v20.12 introduced a new Multi-Core Parallel Computation Algorithm that is key to optimizing your hardware. This is for both the automation and the audio processing. 
<br>
<br>
The **Display Performance** option stated above will be our best ally to monitor the results. This can be accessed with shortcut <code>Shift + Option + Command + P.</code>
<br>
<br>
The Engine Preference section includes 3 Profiles for parallel processing 
![New updated Engine Preference Section](include/engine_profile_1.png)
<br>
<br>
**Automation Rate** provides the ability to set the refresh rate (frequency) of the automation. By default, we use 10.0 ms (100.00 fps). This can be decreased to lower the frequency if you see that automation is becoming a burden for your system with such a fast refresh.
![Automation Rate Optimization](include/engine_profile_4.png)
<br>
<br>
**Max Number of Core** is your ability to make more or fewer cores available to the Spat Revolution algorithm. By default, it will be at your number of native core. Not hyper-threading. This can be increased or reduced. Watch not to take all cores for a multitasking computers.
![Max Number Of Cores - Engine Preference](include/engine_profile_3.png)
<br>
<br>
Lastly are the 3 presets for you to choose from. 
Parallel Profile;
**Max distribution** is for spreading the load as much as possible to all cores mainly with Desktop systems and dedicated real-time spat computers.
<br>
<br>
**Favour First Core**  is a typical preset for Laptop computers where we find that loading cores as much as possible allows us to get out of the way of some of the laptop optimization (power and cooling) that are playing with available processing speed.
<br>
<br>
**Balanced Distribution** is a preset somehow in the middle. It intends to be a balance between both above options.
![Parallel Processing Algo Profile](include/engine_profile_2.png)

---

### Display Performance (CPU) measurements

Included in release version 20.12 is the ability to display performance (CPU) measurements. This can be done in the **Help** menu **Display Performance** option. This can be accesses as well with shortcut <code>Shift + Option + Command + P</code>.

![Inline](include/display_performance.png)

---


### **Clearing Shared Memory**

![inline](include/Clean_Shared_Memory.png)

> If this command is executed, Spat and the plug-in host will then need to be restarted.



^
<br>
Some users have experienced an issue where Spat SEND and RETURN plug-ins are
not cleared from the shared memory when used with certain third-party DAW hosts (or seen after DAW crashes). Although this should not happen and have been intensively improved in the latest releases of Spat Revolution, a **Clean Shared Memory** option can fix some connection issues (ghost modules, duplicated modules, modules not connecting when opening session). 
<br>
<br>
This sometimes can be seen where Spat SEND and RETURN modules appear in the Spat setup page when there is no DAW host software running in the background. It can cause problems, when a host with plugins is launched and more SEND and RETURN plug-ins appear to be doubled.
<br>
<br>
Although rebooting the computer would fix this issue, the workaround if this is happening with your particular 3rd party software, is to invoke a special debug action called _Clean Shared Memory_. It is available by the *Help* menu _Help/Clean Shared Memory_


^
<br>
Some users have experienced issues where Spat SEND and/or RETURN plug-ins are not cleared from memory and will show as ghost input and output modules upon opening the Spat Revolution application. 
<br>
<br>
This could happen with some hosts not properly closing the instances upon quitting and will have the same result if the DAW freezes and gets forced to quit or simply quits unexpectedly.
If this happens, Spat SEND and RETURN modules will appear in the Spat setup editor, when there is no host software running.
<br>
<br>
It can cause problems, when a host with plugins is launched and more SEND and RETURN plug-ins appear to be doubled.  It can create routing issues as well.
<br>
<br>
The workaround, if this is happening with your particular 3rd party software, is to invoke a special debug action in the Spat setup editor. It is called _Clean Shared Memory_. It is available by right-clicking anywhere in the background of the signal graph editor. A pop-up menu will appear with various options and shortcuts. Scroll to the bottom and choose _Help/Clean Shared Memory_

---

## **Rebuilding GUI**

Issues with Graphical User Interface (GUI) could occur, swapping Spat between 2 different screens technologies. If this happening, rebuild the GUI will solve it.
This action is available by right-clicking on the top-bar, or with the shortcut "Shift + Command + F5" on Mac, "Shift + ctrl + F5" on Windows.  

![left](include/Rebuild_GUI.png)

---

* Using terminal for command log 	
* Get and Send source, room and master properties 
* Flush all connections
* Cleaning Shared Memory 
* Rebuilding GUI
* Dealing with Preferences

> WRITER NOTE: This isn't really an "integration" feature. Maybe it could be place in 2.2 Workflow section ?

---

# 3.6 Specification and Hardware Recommendation

[.hide-footer]

---

### Availability

* Spat Revolution is a stand-alone application for MacOS and Windows
* Spat Send/Return/Room plugins are available in AU / VST / AAX Native. 
* Spat Send plugins is available in AAX VENUE.

Plugins Compatibility.
[Access to all Plugins specifications](https://www.flux.audio/plugin-specifications/)

---

### Processing

* Spat Revolution – stand-alone software:
* unlimited number of Input and Output (Hardware and audio interface dependant).
* 32/64-bits internal floating-point processing.
* Sampling rate up to 384 kHz, Block size buffer starting at 16 blocks

---

### OS Compatibility

Windows 10, 64 bits only.
macOS x (Intel) – All versions from 10.12 including macOS Big Sur compliance.

---

### Software Licence Requirements

In order to use the software, an iLok.com user account is required (the iLok USB Smart Key is not required, authorization can be made to hardware machines).


---

# 3.7. Hands-On exercise: SPAT Revolution Integration

Hands-on exercise: (How To) (customized to class)	
[.hide-footer]

---

# 3.7.1 SPAT Revolution Integration


Hands-on exercise: (How To) (customized to class). Hands-on using the third party specific tools


* Creating a DAW session using Spat PI 
* Converting SW to HW setup
* Live consoles
* Building automation to your DAW Application
* Creating OSC Network cues in QLab or other systems   
* Deploying Spat Snapshot systems

---


### Case studies 

* Conventional Panning examples
* Binaural examples
* WFS examples 
* HOA examples                                                                    



---

### Real case studies

!> Need a nice picture here

---

**Immersive super production with Le Cirque Du Soleil**

!> Need a nice picture here

--- 

!> Need a diagram here

---

**Intimist immersive experience with Close Talker**

!> Need a nice picture here

---

<img src="include/closeTalkerBinaural_1.png" alt="Complexe set-up with redundancy" width="700" height="460">

_temporary diagram_

---

**Improving live diffusing using WFS with Neko Light Orchestra**

!> Need a nice picture here

---

<img src="include/nekoWFS.png" alt="Complexe set-up with redundancy" width="850" height="460">

_temporary diagram_

---

**Democratic immersive live with Akagera**

!> Need a nice picture here

---

<img src="include/akagera360_1.png" alt="Complexe set-up with redundancy" width="850" height="460">

_temporary diagram_

---

### 1.2 Spatial audio production ecosystem (Sylvain Cadars)

Encantadas :

Note: 
Présentation projet: Un orchestre séparé en 6 groupes autour du public, avec un dôme ambisonique pour une diffusion à l’ordre 4 ou plus.

L’idée était de reproduire l’espace de l’église de San Lorenzo en Italie à partir de mesures impulsionnelles en IR 3D. Rôle avec Spat Rev : Rendu d’un mix 5.1 à partir de l’enregistrement du concert et des sources ambisoniques.

Les sources : Eigenmike (couple principal), appoints, électronique, arbre 5.0 DPA 4006. Session de travail : Reaper + spat rev sur 2 ordis différents, reliés en MADI, 128 canaux. Retour master dans Reaper pour le REC

---

Fiction Radio :
Présentation projet : Enregistrement de 3 musiciens (percu, cello, flûte) et mixage en HOA ordre 4, pour un rendu sur HP.
Le projet est une fiction sonore autour du livre d’Annie Ernaux « l’autre fille » Ton rôle : Mixeur musique Les sources : Micro d’appoint. Session de travail : Machine locale avec Reaper + Spat Rev. Retour master dans Reaper pour le rec. Projet Eror avec Giorgia Spiropoulos Mise en place d’une session pro tools avec Spat Rev pour la compositrice pour écrire une spatialisation pour un rendu sur une couronne en 6 points.

---

Clément 

Mixage pour un court-metrage VR « A song within us »
Présentation projet : Mixage d’un court-métrage en VR pour un rendu HOA pour enceintes et pour casque / Rendu ordre 4 pour casque VR.
Ton rôle avec spat rev : Rendu d’un mix HOA ordre 4 à partir de la session de montage Sources : Enregistrement B format, multipiste pro tools Session de travail : pro tools -&gt; Reaper, 2 ordinateurs reliés via Dante avec Spat rev. Retour master en HOA ordre 4.