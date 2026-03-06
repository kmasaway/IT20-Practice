import streamlit as st
from datetime import datetime
import time

# Page Configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for unique styling
st.markdown("""
    <style>
    /* Main styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 40px;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .header-title {
        font-size: 3.5em;
        font-weight: bold;
        margin: 0;
    }
    
    .header-subtitle {
        font-size: 1.3em;
        margin: 10px 0 0 0;
        opacity: 0.9;
    }
    
    /* Section styling */
    .section-title {
        color: #667eea;
        font-size: 2em;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
    }
    
    /* Project cards */
    .project-card {
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    /* Skill bar styling */
    .skill-item {
        margin-bottom: 15px;
    }
    
    .skill-name {
        font-weight: bold;
        color: #333;
        margin-bottom: 5px;
    }
    
    .skill-bar {
        background-color: #e0e0e0;
        border-radius: 5px;
        height: 8px;
        overflow: hidden;
    }
    
    .skill-progress {
        display: inline-block;
        height: 100%;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 5px;
    }
    
    /* Contact form styling */
    .contact-section {
        background: white;
        padding: 25px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Social links */
    .social-links {
        display: flex;
        gap: 15px;
        justify-content: center;
        margin: 20px 0;
        flex-wrap: wrap;
    }
    
    .social-link {
        display: inline-block;
        padding: 10px 15px;
        background: #667eea;
        color: white;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        transition: background 0.3s ease;
    }
    
    .social-link:hover {
        background: #764ba2;
    }
    
    /* Metric styling */
    .metric-container {
        display: flex;
        gap: 20px;
        justify-content: space-around;
        margin: 20px 0;
        flex-wrap: wrap;
    }
    
    .metric-card {
        text-align: center;
        padding: 20px;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        min-width: 150px;
    }
    
    .metric-value {
        font-size: 2.5em;
        font-weight: bold;
        color: #667eea;
    }
    
    .metric-label {
        font-size: 0.9em;
        color: #666;
        margin-top: 5px;
    }
    
    /* Navbar styling */
    .navbar {
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 15px 20px;
        border-radius: 8px;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
    }
    
    .navbar-brand {
        color: white;
        font-size: 1.8em;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .navbar-menu {
        display: flex;
        gap: 5px;
        flex-wrap: wrap;
        justify-content: center;
    }
    
    .navbar-button {
        background: rgba(255,255,255,0.2);
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        transition: all 0.3s ease;
        font-size: 0.9em;
    }
    
    .navbar-button:hover {
        background: rgba(255,255,255,0.4);
        transform: translateY(-2px);
    }
    
    .navbar-button.active {
        background: white;
        color: #667eea;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for page selection
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Home"

# Navbar Navigation
navbar_pages = ["🏠 Home", "👤 About", "🛠️ Skills", "📁 Projects", "💼 Experience", "📧 Contact"]

navbar_cols = st.columns([2] + [1]*6)
with navbar_cols[0]:
    st.markdown("""
        <div style="display: flex; align-items: center; padding: 5px;">
            <span style="color: white; font-size: 2em;">🎯 MyPortfolio</span>
        </div>
    """, unsafe_allow_html=True)

for idx, page_name in enumerate(navbar_pages):
    with navbar_cols[idx + 1]:
        if st.button(page_name, use_container_width=True, key=f"nav_{page_name}"):
            st.session_state.page = page_name
            st.rerun()

# Get current page
page = st.session_state.page

st.markdown("---")

# HOME PAGE
if page == "🏠 Home":
    st.markdown("""
        <div class="header-container">
            <h1 class="header-title">📚 Welcome to My Portfolio</h1>
            <p class="header-subtitle">Educator | Passionate Facilitator | BS Secondary Education Graduate</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">150+</div>
                <div class="metric-label">Students Taught</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">8+</div>
                <div class="metric-label">Years in Education</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">95%</div>
                <div class="metric-label">Student Success Rate</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### � My Mission")
        st.info("""
        I am dedicated to inspiring the next generation of learners through engaging, 
        interactive, and inclusive educational practices. With a passion for secondary education, 
        I create meaningful learning experiences that foster critical thinking and lifelong learning.
        """)
    
    with col2:
        st.markdown("### 🎓 My Philosophy")
        st.success("""
        I believe in student-centered learning combined with innovative teaching methodologies. 
        Every lesson is designed with care, cultural sensitivity, and a focus on empowering 
        students to reach their full potential.
        """)

# ABOUT PAGE
elif page == "👤 About":
    st.markdown('<h2 class="section-title">👤 About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://via.placeholder.com/300?text=Your+Photo", use_container_width=True)
        st.markdown("---")
        st.markdown("### 📍 Quick Facts")
        st.write("📧 Email: your.email@example.com")
        st.write("📱 Phone: +1 (XXX) XXX-XXXX")
        st.write("🌍 Location: Your City, Country")
        st.write("🎓 Degree: BS Secondary Education")
        st.write("📚 Teaching Profile: [Your Profile Link]")
    
    with col2:
        st.markdown("""
        ### Hi there! 👋
        
        I'm a dedicated educator and graduate of BS in Secondary Education. Passionate about 
        creating inclusive, engaging, and transformative learning environments. With 8+ years 
        in educational practice, I've had the privilege to work with diverse learners across 
        multiple disciplines and grade levels.
        
        **My Journey:**
        - Earned my BS in Secondary Education with focus on student-centered learning
        - Started teaching in a public high school classroom
        - Developed innovative curriculum and teaching materials
        - Expanded to mentoring new teachers and educational leadership roles
        - Continuously pursuing professional development in pedagogy and technology integration
        
        **What drives me:**
        - Empowering students to think critically and creatively
        - Fostering inclusive learning environments where all students can thrive
        - Integrating technology meaningfully into classroom instruction
        - Supporting fellow educators in their professional growth
        
        **Beyond the Classroom:**
        - Educational workshop facilitator
        - Curriculum design specialist
        - Educational blogger and speaker
        - Lifelong learner and advocate for 21st-century skills
        """)

# SKILLS PAGE
elif page == "🛠️ Skills":
    st.markdown('<h2 class="section-title">🛠️ Skills & Expertise</h2>', unsafe_allow_html=True)
    
    # Filter skills by category
    skill_category = st.selectbox(
        "Filter by category:",
        ["All Skills", "Teaching Methodologies", "Subject Matter", "Technology & Tools", "Leadership"]
    )
    
    skills_data = {
        "All Skills": {
            "Curriculum Design": 95,
            "Student Assessment": 92,
            "Classroom Management": 90,
            "Differentiated Instruction": 88,
            "Educational Technology": 85,
            "Collaborative Learning": 93,
            "Critical Thinking": 92,
            "Digital Literacy": 90
        },
        "Teaching Methodologies": {
            "Inquiry-Based Learning": 92,
            "Problem-Based Learning": 90,
            "Cooperative Learning": 93,
            "Socratic Method": 88,
            "Flipped Classroom": 85,
            "Project-Based Learning": 91
        },
        "Subject Matter": {
            "English Language Arts": 95,
            "Literature Analysis": 93,
            "Writing Instruction": 94,
            "Communication Skills": 92,
            "Research Methods": 90,
            "Grammar & Composition": 95
        },
        "Technology & Tools": {
            "Google Workspace": 92,
            "Learning Management Systems": 90,
            "Digital Presentation Tools": 88,
            "Virtual Classroom Platforms": 85,
            "Educational Apps": 87,
            "Video Production": 80
        },
        "Leadership": {
            "Mentoring & Coaching": 90,
            "Curriculum Leadership": 88,
            "Professional Development": 85,
            "Parent Communication": 92,
            "Team Collaboration": 93,
            "Educational Advocacy": 87
        }
    }
    
    selected_skills = skills_data[skill_category]
    
    col1, col2 = st.columns(2)
    
    skills_list = list(selected_skills.items())
    for idx, (skill, proficiency) in enumerate(skills_list):
        if idx % 2 == 0:
            with col1:
                st.markdown(f"**{skill}**")
                st.progress(proficiency / 100)
        else:
            with col2:
                st.markdown(f"**{skill}**")
                st.progress(proficiency / 100)
    
    st.markdown("---")
    st.markdown("### 📚 Certifications & Credentials")
    cert_col1, cert_col2, cert_col3 = st.columns(3)
    
    certs = [
        ("🏆 BS Secondary Education", "State University"),
        ("🏆 Teaching Certification", "Secondary Education"),
        ("🏆 TESOL Certification", "Professional Development")
    ]
    
    for idx, (cert_title, cert_org) in enumerate(certs):
        if idx % 3 == 0:
            with cert_col1:
                st.success(f"{cert_title}\n\n{cert_org}")
        elif idx % 3 == 1:
            with cert_col2:
                st.success(f"{cert_title}\n\n{cert_org}")
        else:
            with cert_col3:
                st.success(f"{cert_title}\n\n{cert_org}")

# PROJECTS PAGE
elif page == "📁 Projects":
    st.markdown('<h2 class="section-title">📁 Featured Educational Projects</h2>', unsafe_allow_html=True)
    
    # Filter projects
    project_filter = st.selectbox(
        "Filter by type:",
        ["All", "Curriculum", "Research", "Technology", "Workshop"]
    )
    
    projects = [
        {
            "name": "Blended Learning Curriculum for English 101",
            "description": "Comprehensive hybrid curriculum integrating digital tools with traditional instruction for 9th-grade English literature",
            "tech": ["Google Classroom", "Canva", "Padlet", "Nearpod"],
            "link": "https://example.com",
            "category": "Curriculum"
        },
        {
            "name": "Critical Literacy Through Social Justice",
            "description": "Project-based learning sequence exploring contemporary social issues through literary analysis and student voice",
            "tech": ["Discussion Boards", "Documentary Films", "Collaborative Writing"],
            "link": "https://example.com",
            "category": "Curriculum"
        },
        {
            "name": "Digital Storytelling Workshop",
            "description": "Interactive workshop series teaching students multimedia narrative techniques using photography, video, and audio",
            "tech": ["Adobe Creative Suite", "iMovie", "Podcasting"],
            "link": "https://example.com",
            "category": "Workshop"
        },
        {
            "name": "Student Achievement Analysis Study",
            "description": "Mixed-methods research examining the impact of formative assessment on student learning outcomes",
            "tech": ["Qualitative Analysis", "Data Visualization", "Statistical Methods"],
            "link": "https://example.com",
            "category": "Research"
        },
        {
            "name": "Virtual Classroom Environment Setup",
            "description": "Design and implementation of comprehensive virtual learning environment for remote and hybrid instruction",
            "tech": ["Zoom", "Google Meet", "Microsoft Teams", "LMS Integration"],
            "link": "https://example.com",
            "category": "Technology"
        },
        {
            "name": "Peer Teaching Mentorship Program",
            "description": "Structured mentorship initiative training new teachers in evidence-based instructional practices",
            "tech": ["Professional Development", "Coaching", "Collaborative Learning"],
            "link": "https://example.com",
            "category": "Workshop"
        }
    ]
    
    # Filter projects based on selection
    filtered_projects = [p for p in projects if project_filter == "All" or project_filter in p["category"]]
    
    for project in filtered_projects:
        st.markdown(f"""
            <div class="project-card">
                <h3>{project['name']}</h3>
                <p>{project['description']}</p>
                <p><strong>Technologies:</strong> {', '.join(project['tech'])}</p>
                <a href="{project['link']}" target="_blank" class="social-link">View Project →</a>
            </div>
        """, unsafe_allow_html=True)

# EXPERIENCE PAGE
elif page == "💼 Experience":
    st.markdown('<h2 class="section-title">💼 Professional Experience</h2>', unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "Senior Secondary Education Specialist",
            "company": "Metro Public Schools District",
            "period": "Jan 2022 - Present",
            "description": "Lead curriculum development initiatives, mentor new teachers, and facilitate professional development workshops for 50+ educators across multiple departments.",
            "highlights": ["Curriculum Leadership", "Teacher Mentoring", "PD Facilitation"]
        },
        {
            "title": "High School English Teacher",
            "company": "Central High School",
            "period": "Jun 2018 - Dec 2021",
            "description": "Taught grades 9-12 English Language Arts, developed innovative blended learning model, and achieved 92% student proficiency in standardized assessments.",
            "highlights": ["Blended Learning", "Curriculum Design", "Assessment"]
        },
        {
            "title": "Junior High Language Arts Instructor",
            "company": "Lincoln Middle School",
            "period": "Aug 2016 - May 2018",
            "description": "Taught 7th and 8th grade English, implemented project-based learning strategies, and coordinated interdisciplinary units with social studies department.",
            "highlights": ["PBL Implementation", "Differentiation", "Collaboration"]
        },
        {
            "title": "Student Teacher",
            "company": "Roosevelt High School",
            "period": "Jan 2016 - Jun 2016",
            "description": "Completed student teaching practicum while earning BS in Secondary Education, taught multiple sections under mentor teacher supervision.",
            "highlights": ["Teaching Practicum", "Lesson Planning", "Classroom Management"]
        }
    ]
    
    for exp in experiences:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {exp['title']}")
                st.markdown(f"**{exp['company']}** | {exp['period']}")
            with col2:
                st.markdown(f"<div style='text-align: right; color: #667eea; font-weight: bold;'>{exp['period'].split(' - ')[0]}</div>", unsafe_allow_html=True)
            
            st.write(exp['description'])
            
            cols = st.columns(len(exp['highlights']))
            for idx, highlight in enumerate(exp['highlights']):
                with cols[idx]:
                    st.markdown(f"✅ {highlight}")
            
            st.markdown("---")

# CONTACT PAGE
elif page == "📧 Contact":
    st.markdown('<h2 class="section-title">📧 Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📞 Contact Information")
        st.write("📧 **Email:** your.email@example.com")
        st.write("📱 **Phone:** +1 (XXX) XXX-XXXX")
        st.write("🌍 **Location:** Your City, Country")
        st.write("🎓 **School:** Your School Name")
        st.write("📚 **LinkedIn:** linkedin.com/in/yourprofile")
        
        st.markdown("---")
        st.markdown("### 🔗 Professional Links")
        st.markdown("""
            <div class="social-links">
                <a href="https://linkedin.com" class="social-link">LinkedIn</a>
                <a href="https://twitter.com" class="social-link">Twitter</a>
                <a href="https://instagram.com" class="social-link">Instagram</a>
                <a href="https://teachers.com" class="social-link">TeachersPayTeachers</a>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 💬 Send Me a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.selectbox(
                "Subject",
                ["Collaboration Inquiry", "Speaking/Workshop", "Teaching Job", "Other"]
            )
            message = st.text_area("Message", height=150, placeholder="Tell me about your inquiry...")
            
            submitted = st.form_submit_button("Send Message 📨", use_container_width=True)
            
            if submitted:
                if name and email and subject and message:
                    st.success("✅ Message sent successfully! I'll get back to you within 2-3 business days.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all fields.")
    
    st.markdown("---")
    st.markdown("### 📝 Frequently Asked Questions")
    with st.expander("Are you available for speaking engagements or workshops?"):
        st.write("Yes! I'm passionate about professional development and enjoy presenting on topics like blended learning, student engagement, and innovative pedagogy. Let's connect!")
    
    with st.expander("Do you share teaching resources?"):
        st.write("Absolutely! I regularly share curriculum materials, lesson plans, and educational resources through TeachersPayTeachers and my personal blog. Check those platforms for my latest offerings.")
    
    with st.expander("Can we schedule a mentoring session?"):
        st.write("I'm happy to mentor new teachers and educational professionals. Mentoring sessions are available by appointment. Reach out to discuss your specific needs and goals!")
    
    with st.expander("Are you open to curriculum consulting?"):
        st.write("Yes, I offer curriculum development and consulting services for schools and districts looking to enhance their instructional programs. Contact me to learn more about how I can support your institution.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 20px; color: #666;'>
        <p>© 2024 Your Name. All rights reserved.</p>
        <p>Built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
