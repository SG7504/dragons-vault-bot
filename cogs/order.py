import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput

class OrderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def order(self, ctx):
        embed = discord.Embed(
            title="Welcome to Dragon's Vault",
            description="Click below to place an order.",
            color=discord.Color.blue()
        )

        class OrderModal(Modal, title="Order Form"):
            order_details = TextInput(label="Describe your request")

            async def on_submit(self, modal_interaction):
                await modal_interaction.response.send_message("✅ Order received!", ephemeral=True)

        class OrderButton(View):
            @discord.ui.button(label="📩 Place Order", style=discord.ButtonStyle.primary)
            async def place_order(self, interaction, button):
                await interaction.response.send_modal(OrderModal())

        await ctx.send(embed=embed, view=OrderButton())
