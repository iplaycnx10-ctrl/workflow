import streamlit as st


def render_data_workflow_module():
    """Show how business/ad data connects into the working workflow."""

    st.markdown(
        """
        <div class="module-wrap">
            <div class="module-title">00_DATA_TO_WORKFLOW_CONNECTOR</div>
            <p class="module-desc">
                เชื่อมข้อมูลจาก Ads / Line OA / LDP / Pixel / GA4 ให้กลายเป็น Workflow งานจริง:
                รู้ว่าคอขวดอยู่ตรงไหน → ต้องแก้ด้วยทีมไหน → ต้องผลิต Creative หรือปรับระบบอะไรต่อ
            </p>
        """,
        unsafe_allow_html=True,
    )

    c1, a1, c2, a2, c3, a3, c4 = st.columns([1.05, .12, 1.05, .12, 1.05, .12, 1.05])

    with c1:
        st.markdown(
            """
            <div class="card pastel-blue">
                <span class="pill top">DATA INPUT</span>
                <h3>ข้อมูลที่ต้องเก็บ</h3>
                <p>
                    <b>Ads:</b> Spend, CPM, CTR, CPC, Inbox, Purchase, ROAS<br>
                    <b>LDP:</b> Click, View, CTA Click, Form/Line Click<br>
                    <b>Line OA:</b> Add friend, Chat, Close, Reason lost<br>
                    <b>GA4/Pixel:</b> ViewContent, ATC, IC, Purchase
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with a1:
        st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(
            """
            <div class="card pastel-pink">
                <span class="pill pink">DIAGNOSIS</span>
                <h3>อ่านคอขวด</h3>
                <p>
                    CTR ต่ำ = CI / Hook ยังไม่ดึง<br>
                    Inbox เยอะแต่ปิดไม่ได้ = Offer / Trust / Admin<br>
                    Click เยอะแต่ไม่ Add Line = LDP / CTA ไม่ชัด<br>
                    Event หาย = Pixel / GTM / Tracking ต้องแก้ก่อน
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with a2:
        st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)

    with c3:
        st.markdown(
            """
            <div class="card pastel-lav">
                <span class="pill mid">WORKFLOW ROUTE</span>
                <h3>ส่งเข้าทีมทำงาน</h3>
                <p>
                    <b>CI Problem:</b> ส่งเข้า Creative Brief<br>
                    <b>LDP Problem:</b> ส่งเข้าแผนปรับหน้าเว็บ<br>
                    <b>Tracking Problem:</b> ส่งเข้า Pixel / GA4<br>
                    <b>Close Problem:</b> ส่งเข้า Admin Checklist
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with a3:
        st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)

    with c4:
        st.markdown(
            """
            <div class="card pastel-mint">
                <span class="pill bot">ACTION OUTPUT</span>
                <h3>ผลลัพธ์ที่ต้องได้</h3>
                <p>
                    1) วันนี้ต้องทำ Creative อะไร<br>
                    2) ต้องแก้ LDP จุดไหน<br>
                    3) Pixel/GA4 event ไหนต้องเช็ก<br>
                    4) แอดมินต้องเก็บเหตุผลปิดไม่ได้อะไร<br>
                    5) วันถัดไป Scale / Hold / Fix / Kill
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="visual-flow">
            <div class="merge-node pastel-amber">
                <span class="pill amber">WORKFLOW RULE</span>
                <h4>หลักการเชื่อมข้อมูล</h4>
                <p>
                    อย่าให้ข้อมูลเป็นแค่รายงานย้อนหลัง แต่ต้องแปลงเป็นงานทันที:<br>
                    <b>Metric → Problem → Owner → Task → Deadline → Next Check</b>
                </p>
            </div>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
