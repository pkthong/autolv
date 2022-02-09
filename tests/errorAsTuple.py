# %%
import autolv
lv = autolv.App()
vi = lv.open('error.vi')

# %%
vi.myCode = -1126
await vi.run()

# %%
code = vi["error out"]
print(code)
# %%
print (vi["error out"])
# %%
print (vi._ctrls)
# %%
