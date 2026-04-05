# Cyber Security

**Subject:** Science & Technology > IT & Communication
**Syllabus ID:** S&T.IT.1
**Total Questions:** 7 (Prelims: 5, Mains: 2)
**Year Range:** 2011 – 2020
**Last Asked:** 2020
**Revision Priority:** 🟡 MEDIUM

## Keywords
cryptography, e-governance, digital signature, authentication, IT Act, PKI, cyber security, cloud hosting, cybersecurity, MeghRaj

## Dimensions Tested
- **WHAT**: 5 questions
- **VS**: 1 questions
- **WHO**: 1 questions

## Related Concepts
- SSL/TLS
- Digital signature
- Aadhaar authentication
- Cyber security
- Certificate Authority
- Personal Data Protection Bill
- NPCI
- SSL/TLS certificates

## Prelims Questions

### 🔴 HIGH Priority — Full MCQ + Trap Intelligence

*Use these verbatim as Practice MCQs in CDF notes.*

**[Q2940]** [2019]
> Consider the following statements: The Reserve Bank of India's recent directives relating to 'Storage of Payment System Data', popularly known as data diktat, command the payment system providers that  1. they shall ensure that entire data relating to payment systems operated by them are stored in a system only in India 2. they shall ensure that the systems are owned and operated by public sector enterprises 3. they shall submit the consolidated system audit report to the Comptroller and Auditor General of India by the end of the calendar year  Which of the statements given above is/are correct?

  ✅ A) 1 only
     B) 1 and 2 only
     C) 3 only
     D) 1, 2 and 3

  ⚠️ **Trap:** Statements 2 and 3 are traps — RBI's data localisation order does NOT require public sector ownership of systems, nor does it involve CAG audit. Only statement 1 (data stored only in India) is correct.
  💡 **Eliminate:** RBI's 2018 data localisation circular: payment data must be stored only in India (statement 1 correct); no requirement of public sector ownership (statement 2 wrong); no CAG audit requirement (statement 3 wrong). Answer is A.
  📌 **Key facts:**
     - RBI Data Lokalization Circular 2018: all payment system data must be stored within India
     - No mandate for public sector system ownership — private players like Visa, Mastercard also covered
     - CAG has no role in payment system data audit — RBI is the regulator

**[Q2941]** [2019]
> Which of the following adopted a law on data protection and privacy for its citizens known as 'General Data Protection Regulation' in April 2016 and started implementation of it from 25th May, 2018?

     A) Australia
     B) Canada
  ✅ C) The European Union
     D) The United States of America

  ⚠️ **Trap:** Candidates may confuse GDPR with US privacy legislation (CCPA — California Consumer Privacy Act) or assume it was adopted by the UN. GDPR is a distinctly EU regulation.
  💡 **Eliminate:** GDPR = General Data Protection Regulation adopted by European Union in April 2016, implemented from May 25, 2018. Answer is C.
  📌 **Key facts:**
     - GDPR adopted by EU Parliament April 2016, effective May 25, 2018
     - Applies to all companies processing EU citizens' data globally — extraterritorial reach
     - Heavy penalties: up to 4% of global annual revenue or €20 million

**[Q2948]** [2019]
> Consider the following statements : A digital signature is  1. an electronic record that identifies the certifying authority issuing it 2. used to serve as a proof of identity of an individual to access information or server on Internet 3. an electronic method of signing an electronic document and ensuring that the original content is unchanged  Which of the statements given above is/are correct?

     A) 1 only
     B) 2 and 3 only
  ✅ C) 3 only
     D) 1, 2 and 3

  ⚠️ **Trap:** Statement 1 is a trap — a digital signature identifies the signatory/certificate holder, not the certifying authority per se. Statement 2 about identity verification is a function of digital certificates, not digital signatures specifically. Only statement 3 correctly describes digital signature.
  💡 **Eliminate:** A digital signature primarily ensures authenticity and integrity of an electronic document (statement 3). It does not identify the certifying authority (statement 1 wrong) nor is it used for server access like a password (statement 2 wrong). Answer is C.
  📌 **Key facts:**
     - Digital signature = cryptographic mechanism to verify identity of sender and integrity of message
     - Uses public-private key cryptography; ensures document not tampered after signing
     - IT Act 2000 gives legal validity to digital signatures in India

**[Q3467]** [2011]
> What is "Virtual Private Network"?

     A) It is a private computer network of an organization where the remote users can transmit encrypted information through the server of the organization
  ✅ B) It is a computer network across a public internet that provides users access to their organization's network while maintaining the security of the information transmitted
     C) It is a computer network in which users can access a shared pool of computing resources through a service provider
     D) None of the statements (a), (b) and (c) given above is a correct description of Virtual Private Network

  ⚠️ **Trap:** Option A sounds similar but specifies 'encrypted information through server of the organization' — VPN uses a public internet, not just organization's server; option C describes cloud computing.
  💡 **Eliminate:** VPN = secure access to organization's network over public internet with encryption. Option B correctly describes this. Option A describes a private intranet; option C describes cloud computing.
  📌 **Key facts:**
     - VPN (Virtual Private Network): creates encrypted tunnel over public internet for secure remote access to private network
     - Used by organizations for secure remote work, bypassing geo-restrictions, and privacy protection

### 🟡 MEDIUM Priority — Full Options

**[Q3001]** [2020] In India, the term "Public Key Infrastructure" is used in the context of

  ✅ A) Digital security infrastructure
     B) Food security infrastructure
     C) Health care and education infrastructure
     D) Telecommunication and transportation infrastructure

  ⚠️ **Trap:** Options B, C and D seem plausible in the context of government infrastructure, but PKI is specifically a digital security framework involving encryption keys and certificates.

## Mains Questions

*Each question includes answer framework with word budget.*

### GS3

**[2015]** Q13. Discuss the advantages and security implications of cloud hosting of servers vis-a-vis in-house machine-based hosting for government businesses. (200 words) 12.5
  *Paper: GS3 | Dim: VS | 12.5m | ~200w*
  🏷️ Themes: E-governance security, Cloud adoption, Digital infrastructure

  **Answer Framework:**
  *(~200 words: intro 30w / body 130w / conclusion 40w)*
  - 🔑 **Intro:** The shift from in-house machine-based hosting to cloud hosting for government services presents significant advantages in cost and scalability but also raises critical security and sovereignty concerns.
  - 📋 **Body:**
      • Advantages of cloud: cost efficiency, scalability, disaster recovery, reduced IT maintenance
      • Security implications: data breach risk, vendor lock-in, jurisdictional issues, foreign surveillance
      • Government's GI Cloud (MeghRaj) initiative to address sovereignty concerns
      • Need for stringent SLAs, encryption, audit mechanisms
  - 🎯 **Conclusion:** A hybrid cloud model with robust data protection norms can allow governments to leverage cloud benefits while safeguarding national security.
  🔗 Interlinkages: E-governance, Cyber security policy, Internal security
  🌐 Contemporary: India's increasing digital governance footprint makes secure cloud architecture a critical national priority.

**[2013]** Q16. (a) What is a digital signature ? What does its authentication mean ? Give various salient built-in features of a digital signature. [100 words] 5
  *Paper: GS3 | Dim: WHAT | 5m | ~100w*
  🏷️ Themes: Digital security, e-Governance infrastructure, Trust in digital transactions

  **Answer Framework:**
  *(~100 words: intro 30w / body 80w / conclusion 25w)*
  - 🔑 **Intro:** Digital signatures provide cryptographic authentication that ensures document integrity, non-repudiation, and signer identity in electronic transactions.
  - 📋 **Body:**
      • Definition: encrypted hash of document created with signer's private key, verifiable by public key
      • Authentication: confirms identity of signer via certificate from licensed Certifying Authority
      • Features: tamper-evident (hash changes if document altered), non-repudiation, time-stamping
      • Legal basis: IT Act 2000, Sec 3 recognizes digital signatures; CCA oversees CAs
      • Applications: e-tendering, income tax filing, MCA21 portal, court filings
  - 🎯 **Conclusion:** Digital signatures are foundational to India's digital economy, providing the trust infrastructure for secure e-governance and commerce.
  🔗 Interlinkages: GS3 – Science & Technology, GS2 – E-Governance, GS3 – Internal Security
  🌐 Contemporary: Expanding e-governance and digital financial services make digital signature infrastructure increasingly critical.

## Cross-Paper Transfer

*Use these when this topic appears in other GS papers or Essay.*

### GS Paper Connections
- E-governance
- Cyber security policy
- Internal security
- GS3 – Science & Technology
- GS2 – E-Governance
- GS3 – Internal Security

### Essay & Thematic Angles
- E-governance security
- Cloud adoption
- Digital infrastructure
- Digital security
- e-Governance infrastructure
- Trust in digital transactions

### Contemporary Relevance
Expanding e-governance and digital financial services make digital signature infrastructure increasingly critical.

## Exam Patterns & Insights

- **Most tested dimension:** WHAT (5/7 = 71% of questions)
- **Question types (Prelims):** Factual: 5
- **Recent frequency (2020–2025):** 1 questions

### Common Trap Patterns on This Topic
- Statements 2 and 3 are traps — RBI's data localisation order does NOT require public sector ownership of systems, nor does it involve CAG audit. Only statement 1 (data stored only in India) is correct.
- Candidates may confuse GDPR with US privacy legislation (CCPA — California Consumer Privacy Act) or assume it was adopted by the UN. GDPR is a distinctly EU regulation.
- Statement 1 is a trap — a digital signature identifies the signatory/certificate holder, not the certifying authority per se. Statement 2 about identity verification is a function of digital certificates, not digital signatures specifically. Only statement 3 correctly describes digital signature.
- Options B, C and D seem plausible in the context of government infrastructure, but PKI is specifically a digital security framework involving encryption keys and certificates.
- Option A sounds similar but specifies 'encrypted information through server of the organization' — VPN uses a public internet, not just organization's server; option C describes cloud computing.
