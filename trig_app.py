            st.pyplot(fig)

            # حفظ الصورة
            fig.savefig("graph.png")
            with open("graph.png", "rb") as f:
                st.download_button(
                    "💾 تحميل الرسم كصورة",
                    f,
                    file_name="graph.png",
                    mime="image/png"
                )

    except:
        st.error("❌ المعادلة غير صحيحة")

elif clear_plot:
    st.info("تم مسح الرسم ✨")

# ================== التذييل ==================
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>"
    "<b>الاسم:</b> يوسف<br>"
    "<b>الصف:</b> عاشر \"ب\""
    "</div>",
    unsafe_allow_html=True
)
