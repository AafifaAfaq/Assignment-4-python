import streamlit as st
import time

# Set page config
st.set_page_config(page_title="Countdown Timer ⏱️", layout="centered")
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>⏳ Countdown Timer</h1>", unsafe_allow_html=True)

# Initialize session state
defaults = {
    'duration': 60,
    'running': False,
    'start_time': None,
    'remaining': None,
    'paused': False,
    'pause_start': None,
    'total_pause_time': 0,
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# Duration input
with st.expander("⏱️ Set Timer Duration", expanded=not st.session_state.running):
    col1, col2 = st.columns(2)
    with col1:
        minutes = st.number_input("Minutes", min_value=0, max_value=60, value=1)
    with col2:
        seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0)
    total_seconds = minutes * 60 + seconds

# Timer display
if st.session_state.running:
    if st.session_state.paused:
        elapsed = st.session_state.remaining
    else:
        elapsed = time.time() - st.session_state.start_time - st.session_state.total_pause_time
        st.session_state.remaining = max(0, st.session_state.duration - elapsed)

    mins, secs = divmod(int(st.session_state.remaining), 60)
    time_display = f"{mins:02d}:{secs:02d}"

    st.markdown(f"""
    <h2 style='text-align: center; font-size: 48px; color: #ff9900;'>{time_display}</h2>
    """, unsafe_allow_html=True)

    progress = 1 - (st.session_state.remaining / st.session_state.duration)
    st.progress(min(1.0, progress))

    if st.session_state.remaining <= 0 and not st.session_state.paused:
        st.success("⏰ Time's up!")
        st.balloons()
        st.session_state.running = False
    elif not st.session_state.paused:
        time.sleep(0.1)
        st.rerun()
else:
    st.markdown(f"<h2 style='text-align:center;'>Set Time: {minutes:02d}:{seconds:02d}</h2>", unsafe_allow_html=True)

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if not st.session_state.running:
        if st.button("▶️ Start", use_container_width=True):
            st.session_state.duration = total_seconds
            st.session_state.running = True
            st.session_state.start_time = time.time()
            st.session_state.paused = False
            st.session_state.total_pause_time = 0
            st.rerun()

with col2:
    if st.session_state.running:
        if st.session_state.paused:
            if st.button("⏯️ Resume", use_container_width=True):
                pause_duration = time.time() - st.session_state.pause_start
                st.session_state.total_pause_time += pause_duration
                st.session_state.paused = False
                st.rerun()
        else:
            if st.button("⏸️ Pause", use_container_width=True):
                st.session_state.paused = True
                st.session_state.pause_start = time.time()
                st.rerun()

with col3:
    if st.session_state.running:
        if st.button("🔁 Reset", use_container_width=True):
            for key in defaults:
                st.session_state[key] = defaults[key]
            st.rerun()
